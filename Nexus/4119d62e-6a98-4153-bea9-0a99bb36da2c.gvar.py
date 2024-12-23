# Thanks for using BagLib
# created by:
# Discord: byronius; GitHub: LazyDope; Ko-Fi: alazydope

# Define constants
asterisk = '\\*'
openModes = ["none", "one", "all"]
longModes = ["truncate", "newrow", "newline"]
doesntdont = ["doesn't", "don't"]
ch = character()
a_bag = [str, dict]

# Load user variable
DEFAULT_COIN_RATES = {"pp": 0.1, "gp": 1, "ep": 2, "sp": 10, "cp": 100}
DEFAULT_COIN_EMOJIS = {
    "cp": "<:DDBCopper:953399505129205830>",
    "sp": "<:DDBSilver:953399505124995122>",
    "ep": "<:DDBElectrum:953399505129205831>",
    "gp": "<:DDBGold:953399505062080594>",
    "pp": "<:DDBPlatinum:953399504739106847>"
}
COIN_RATES = list((load_yaml((get_svar("coinRates") or ch.get_cvar("coinRates", "[]")).lower()) or DEFAULT_COIN_RATES).items())
COIN_RATES.sort(key=lambda x: x[1])
COIN_RATES = dict(COIN_RATES)
COIN_TYPES = list(COIN_RATES)
DEFAULT_COIN = [coin for coin, rate in COIN_RATES.items() if rate == 1]
DEFAULT_COIN = DEFAULT_COIN[0] if DEFAULT_COIN else COIN_TYPES[0]
coinPouchName = get_svar("coinPouchName") or ch.get_cvar("coinPouchName", "Coin Pouch")
coinWeighs = float(get_svar("coinWeighs") or ch.get_cvar("coinWeighs", 0.02))

ITEM_PREFIXES = load_yaml(var) if (var := get_svar("bagItemPrefixes") or ch.get_cvar("bagItemPrefixes")) is not None else DEFAULT_COIN_EMOJIS

default_packs = load_yaml(get_gvar("c81ff7db-ae6e-439e-8b54-7170bbefd0fe"))
hb_packs = load_yaml(get_svar("extraPacks", '[]'))+load_yaml(ch.get_cvar("extraPacks", '[]'))

packs = default_packs + hb_packs

pbRaces = ["bugbear", "firbolg", "goliath", "orc"]
pbRaces = pbRaces+(hb_pbRaces := load_yaml(ch.get_cvar("powerfulBuildRaces", "[]").lower())+load_yaml(get_svar("powerfulBuildRaces", "[]").lower()))

default_settings = {
    "weightlessBags": [
        "bag of holding",
        "handy haversack",
        "heward's handy haversack"
    ],
    "customWeights": {},
    "weightTracking": "Off",
    "openMode": "All",
    "encumbrance": "Off",
    "autoCoins": False
}
settings = load_yaml(ch.get_cvar("bagSettings", dump_json(default_settings)))
if not "openMode" in settings or not settings.openMode.lower() in openModes:
    settings.update({"openMode": "All"})
if not "encumbrance" in settings:
    settings.update({"encumbrance": "Off"})
if not "autoCoins" in settings:
    settings.update({"autoCoins": False})

weightDict = load_yaml(get_gvar("9eac80b1-1e1a-41ea-9a99-81a5f0f3be8e"))
custWeights = settings.get('customWeights', {})
if typeof(server_weights := load_yaml(get_svar("bag_custom_weights", "{}"))) == "SafeList":
    for item in server_weights:
        if typeof(item) == "str":
            weightDict.update(load_yaml(get_gvar(item)))
        else:
            weightDict.update(item)
else:
    weightDict.update(server_weights)
weightDict.update(custWeights)

carryMod = ch.stats.strength*(
    2 if ch.get_cvar('race', ch.race).lower() in pbRaces else 1
)*(
    2 if load_yaml(ch.get_cvar('subclass', '{}')).get("BarbarianLevel", "") == "Totem Warrior"
    and ch.get_cvar("l6totem", "") == "Bear" else 1
)


# Define functions
def load_bags(ch=character(), cvar="bags") -> [a_bag]:
    """
    Loads the current character's bags as a list.
    :var ch: The current character, will be loaded if none is provided. default: character()
    :return: a list of bags
    :rtype: [a_bag]
    """

    # grab the list of cvars
    cvars = ch.cvars

    # update legacy bags to new format
    if cvar == "bags":
        old_bags = [load_yaml(cvars[x]) for x in cvars if "bag" in x and x.strip("bag").isdecimal()]
        old_bags_converted = [[bag[0],{bag[item_index].i:bag[item_index].q for item_index in range(1,len(bag))}] for bag in old_bags]
        for i in range(len(old_bags)):
            ch.delete_cvar(f"bag{i}")

    # load bags
    bagsLoaded = load_yaml(ch.get_cvar(cvar, '[]'))
    bagsLoaded = bagsLoaded + old_bags_converted

    # remove duplicate names
    bag_names = [bag[0] for bag in bagsLoaded]
    if (dupe_bags := [bag_name for bag_name in set(bag_names) if bag_names.count(bag_name)>1]):
        for bag in bagsLoaded[::-1]:
            if bag[0] in dupe_bags:
                i = int(num) if (num:=bag[0].split(' ')[-1]).isdecimal() else 1
                dupe_bags.remove(bag[0])
                while [bag[0] for bag in bagsLoaded].count(bag[0]) > 1:
                    i += 1
                    bag[0] = f"""{bag[0].rstrip(" 1234567890")} {i}"""

    # remove entries with 0 items
    for bag in bagsLoaded:
        if bag[0] == coinPouchName:
            bag[1] = {item: count for item, count in bag[1].items() if count > 0 or item in COIN_TYPES}
        else:
            bag[1] = {item: count for item, count in bag[1].items() if count > 0}

    # makes sure if bags are used, variables follow character
    for var in ['coinRates', 'coinPouchName', 'coinWeighs']:
        if (svar := get_svar(var)):
            ch.set_cvar(var, svar)

    return bagsLoaded


def save_bags(bagsLoaded: list, error=False, ch=character(), cvar="bags") -> int:
    """
    Saves the current bag configuration.
    :arg list bagsLoaded: The dict or list of bags
    :var bool error: Whether an error occurred before trying to save default: False
    :var ch: The current character default: character()
    :return: the success state; 0 for no bags, 1 for success, and -1 for failure
    :rtype: int
    """
    # check if there was an error, or if the provided bags are in the wrong format
    if error or typeof(bagsLoaded) not in ['SafeDict', 'SafeList']:
        return -1

    # if there are no more bags, remove the bags cvar
    elif not bagsLoaded:
        ch.delete_cvar(cvar)
        return 0

    # dumb the bags in the appropriate way
    elif typeof(bagsLoaded) == 'SafeDict':
        ch.set_cvar(cvar, dump_json(list(bagsLoaded.items())))
    else:
        ch.set_cvar(cvar, dump_json(bagsLoaded))
    return 1


def get_bag(bagsLoaded: list, bag_id, exact_match=False, create_on_fail=False) -> a_bag:
    """
    Retrieves a bag from the provided list, given the name or index.
    :arg list bagsLoaded: the list of bags to search
    :arg str|int bag_id: the identifier, either index or name, to try to find
    :var bool exact_match: whether to only return the bag if it's an exact match default: False
    :var bool create_on_fail: whether to create a new bag if one is not found default: False
    :return: the bag that matches the request if it could be found.
    :rtype: a_bag
    """
    bagsLoaded = _as_list(bagsLoaded)  # ensure bags are in list format

    # try to grab the bag from the list position
    if typeof(bag_id) == 'int':
        position = max(min(len(bagsLoaded)-1, bag_id), 0)
        bag = bagsLoaded[position]
        return bag

    # try to grab the bag by name, getting progressivly fuzzier if an exact match is not needed
    bag = [b for b in bagsLoaded if b[0] == bag_id]
    if not bag and not exact_match:
        bag = [b for b in bagsLoaded if bag_id.lower() == b[0].lower()]
    if not bag and not exact_match:
        bag = [b for b in bagsLoaded if bag_id in b[0]]
    if not bag and not exact_match:
        bag = [b for b in bagsLoaded if bag_id.lower() in b[0].lower()]

    # create a new bag if the argument is enabled
    if not bag and create_on_fail:
        return new_bag(bagsLoaded, bag_id)
    # return the bag
    if not bag:
        return None
    else:
        return bag[0]


def new_bag(bagsLoaded: list, bag_name="New Bag") -> a_bag:
    """
    Creates a new bag with the given name.
    Will try to find an unused name if the given one is not available
    :arg list bagsLoaded: the list of bags to create in
    :var str bag_name: the name of the new bag default: "New Bag"
    :return: the new bag
    :rtype: a_bag
    """
    bag_name = bag_name or "New Bag"
    bagsLoaded = _as_list(bagsLoaded)
    bag_name = find_valid_name(bagsLoaded, bag_name)  # check for a name that is unused
    bagsLoaded.append([bag_name, {coin: 0 for coin in COIN_TYPES} if bag_name == coinPouchName else {}])
    return bagsLoaded[-1]


def modify_item(
    bagsLoaded: list,
    item: str = None,
    quantity: int = 0,
    bag_name: str = None,
    create_on_fail: bool = False,
    recursive_search: bool = False,
    delta: dict = {},
    conversion_rates: dict = {}
) -> (a_bag, list, bool):
    """
    Modifies an item in a bag by a given quantity.
    :arg list bagsLoaded: the list of bags to modify
    :var str item: the name of the item to modify default: None
    :var int quantity: the delta of the item to modify, positive adds, negative removes default: 0
    :var str bag_name: the desired bag to search in, otherwise uses the first bag with the item already in it default: None
    :var bool create_on_fail: whether to create a new bag if one is not found default: False
    :var bool recursive_search: whether to search for other bags that contain the requested item, only if quantity is negative default: False
    :var dict delta: instead of item, quantity, a dict of item quantity deltas can be provided and handled instead. All deltas must be int. default: {}
    :var dict conversion_rates: the rates at which to convert one item to another. Eg. 0.1:10 = 1:100 ratio. If a conversion rate is present, will try to convert instead of searching recusively. default: {}
    :return: the bag modified, all the final item names, and an error bool
    :rtype: (a_bag, list, bool)
    """
    # setup variables
    bagsLoaded = _as_list(bagsLoaded)
    bag = None
    error = True
    quantity = int(quantity)
    delta.update({item: delta.get(item, 0)+quantity} if item and quantity else {})

    # try to find a bag with the given name, failing to do so, fallback to searching for a bag with the item already in it
    if bag_name:
        bag = get_bag(bagsLoaded, bag_name)
    if not bag:
        for item in delta:
            bag = find_bag_with_item(bagsLoaded, item)
            recursive_search = True
            if bag:
                break

    # create a new bag if the option is set, otherwise grab the first bag in the list
    if bag_name and not bag and create_on_fail:
        bag = new_bag(bagsLoaded, bag_name)
    if not bag and len(bagsLoaded) > 0:
        bag = get_bag(bagsLoaded, 0)
    if not bag and create_on_fail:
        bag = new_bag(bagsLoaded)
    if not bag:
        return (bag_name, error)

    all_item_names = []
    for item in delta:
        # try to find the closest match for the item we want, ignoring case
        item_names = [x for x in bag[1] if item.lower() == x.lower()] + ([x for x in bag[1] if item.lower() in x.lower()] if quantity < 0 else [])
        item_name = item_names[0] if item_names else item
        all_item_names.append(item_name)

        # save the current quantity of the item, then make sure that we have enough of the item in the bag
        c_value = bag[1][item_name] if item_names else 0
        if c_value >= -delta[item] or conversion_rates:
            # load conversion rates in the correct order
            if conversion_rates:
                conversion_rates = list(conversion_rates.items())
                conversion_rates.sort(key=lambda x: x[1])
                conversion_rates = dict(conversion_rates)
            conversion_types = list(conversion_rates)
            index = conversion_types.index(item_name) if item_name in conversion_types else None
            # update the bag's values, remove the entry if it's empty
            bag[1][item_name] = remainder = (c_value + delta[item])
            error = False
            # convert if possible
            if index and remainder < 0:
                for item_type in conversion_types[:index-1:-1]:
                    if bag[1][item_type] < 0:
                        larger = conversion_types[conversion_types.index(item_type)-1]
                        ratio = _get_ratio(conversion_rates[larger], conversion_rates[item_type])
                        p = bag[1][item_type]//ratio[1]
                        bag[1].update({larger: int(bag[1].get(larger, 0)+p*ratio[0]), item_type: int(bag[1].get(item_type, 0)-p*ratio[1])})
                        bag[1].pop(larger) if bag[1][larger] == 0 else ()
                        bag[1].pop(item_type) if item_type != item_type and bag[1][item_type] == 0 else ()
                error = any([bag[1][item_type] < 0 for item_type in bag[1]])
            elif remainder < 0 and recursive_search:
                return _remove_item_recursive(bagsLoaded, item, remainder, bag[0])
            if bag[1][item_name] <= 0:
                bag[1].pop(item_name)
    return (bag, all_item_names, error)


def _remove_item_recursive(bagsLoaded: list, item: str, remainder: int, first_bag: str = None) -> a_bag:
    """
    Handles fuzzy item removal from multiple bags if there is not enough in a single bag
    :arg list bagsLoaded: the list of bags
    :arg str item: the name of the item you're trying to remove
    :arg int remainder: how many more of the item you need to remove
    :return: a bag representing the bags accessed
    :rtype: a_bag
    """
    # define variables
    bagsLoaded = _as_list(bagsLoaded)
    total_items = 0
    names = [first_bag] if first_bag else []

    # loop though each bag, removing as many of the item as possible until remainder consumed
    for bag in bagsLoaded:
        item_names = [x for x in bag[1] if item.lower() == x.lower()]
        item_name = item_names[0] if item_names else item
        c_value = bag[1][item_name] if item_names else 0
        total_items += c_value
        if c_value > 0 and remainder < 0:
            names.append(bag[0])
            bag[1][item_name] = (remainder := remainder + c_value)
            # remove entry if empty
            if remainder < 1:
                bag[1].pop(item_name) if item_names else ()

    # show in one bag mode that multiple bags were used
    if len(names) > 1:
        names[-1] = "and " + names[-1]
    if remainder < 0:
        return ([", ".join(names), {item: total_items}], True)
    else:
        return ([", ".join(names), {item: total_items}], False)


def modify_coins(
    bagsLoaded: list,
    coin: str = DEFAULT_COIN,
    quantity: float | int = 0,
    delta: dict = {},
    autoCoins: bool = settings.get('autoCoins', get("autocoins", "0")=="1"),
    ch=character()
) -> (a_bag, bool):
    """
    Modifies the coin pouch or coin purse automatically.
    Handles automatic switching depending if non-standard coins are in use.
    Returns the coin bag or a bag representing the coin purse, as well as a bool for error handling
    :arg list bagsLoaded: list of all the bags
    :var str coin: the coin that is being modified default: self.DEFAULT_COIN
    :var float|int quantity: how much to change the coins by default: 0
    :var dict delta: instead of coin or quantity you can provide delta, a dict of coins and quantities default: {}
    :var bool autoCoins: whether to convert into larger denominations default: self.settings.autoCoins
    :var ch: the character, can be passed through if already loaded default: character()
    :return: a bag representing the coins accessed, and an error bool
    :rtype: (a_bag, bool)
    """
    # define variables
    bagsLoaded = _as_list(bagsLoaded)
    pouch = get_coins(bagsLoaded, autoCoins=False, ch=ch)
    max_i = len(COIN_TYPES) - 1

    # prepare the coin diff
    if quantity:
        delta[coin] = delta.get(coin, 0)+quantity

    # check if coins are valid
    if any([coin.lower() not in COIN_TYPES for coin in delta]):
        return pouch, True
    delta = delta.copy()

    # smooth out any floating point entries
    for i, coin in enumerate(COIN_TYPES[:-1]):
        if (decimal := abs(delta.get(coin, 0)) % 1):
            smaller = COIN_TYPES[i+1]
            rate = COIN_RATES[smaller]/COIN_RATES[coin]
            sign = delta[coin]/abs(delta[coin])
            p = round(decimal*rate, max_i - i)
            delta.update({
                smaller: delta.get(smaller, 0)+sign*p,
                coin: delta.get(coin, 0)-sign*decimal
            })

    # finally ensure all are int
    for coin_type in delta:
        delta[coin_type] = round(delta[coin_type])

    # prepare coins regardless of if it's coin pouch or coin purse
    negative = False
    for coin_type in delta:
        pouch[1][coin_type] += delta[coin_type]
        negative = negative or delta[coin_type] < 0

    # after modifying the coins, do autoconversions, and check if you actually have enough
    if negative:
        for i, coin_type in enumerate(COIN_TYPES[::-1]):
            if i == max_i and pouch[1][coin_type] >= 0:
                negative = False
            elif i != max_i and pouch[1][coin_type] < 0:
                larger = COIN_TYPES[max_i-i-1]
                ratio = _get_ratio(COIN_RATES[larger], COIN_RATES[coin_type])
                p = pouch[1][coin_type]//ratio[1]
                pouch[1].update({
                    larger: int(pouch[1][larger]+p*ratio[0]),
                    coin_type: int(pouch[1][coin_type]-p*ratio[1])
                })

    # if largest coin still negative, convert as necessary
    if negative and not autoCoins:
        for i, coin_type in enumerate(COIN_TYPES[:-1]):
            if pouch[1][coin_type] < 0:
                smaller = COIN_TYPES[i+1]
                ratio = _get_ratio(COIN_RATES[smaller], COIN_RATES[coin_type])
                p = pouch[1][coin_type]//ratio[1]
                pouch[1].update({
                    smaller: int(pouch[1][smaller]+p*ratio[0]),
                    coin_type: int(pouch[1][coin_type]-p*ratio[1])
                })

    # convert into higher denominations if the setting is enabled
    if autoCoins:
        for i, coin_type in enumerate(COIN_TYPES[-2::-1]):
            smaller = COIN_TYPES[max_i-i]
            ratio = _get_ratio(COIN_RATES[smaller], COIN_RATES[coin_type])
            p = pouch[1][smaller]//ratio[0]
            if p:
                pouch[1].update({
                    smaller: int(pouch[1][smaller]-p*ratio[0]),
                    coin_type: int(pouch[1][coin_type]+p*ratio[1])
                })

    if any([pouch[1][coin_type] < 0 for coin_type in pouch[1]]):
        return (pouch, True)

    # if the modifications were successful, dump to actual coin purse
    if use_coin_purse(bagsLoaded):
        ch.coinpurse.set_coins(pouch[1].pp, pouch[1].gp, pouch[1].ep, pouch[1].sp, pouch[1].cp)
    return (pouch, False)


def get_coins(bagsLoaded: list, autoCoins=settings.get('autoCoins', get("autocoins", "0") == "1"), ch=character()) -> a_bag:
    """
    Returns a bag of how many coins you currently have.
    Will not update your coins if modified.
    :arg list bagsLoaded: a list of bags
    :var bool autoCoins: whether to convert coins into larger denominations default: self.settings.autoCoins
    :var ch: your character default: character()
    :return: a bag representing your coins
    :rtype: a_bag
    """
    # check if we are using coin purse or not
    if autoCoins:
        pouch, _ = modify_coins(bagsLoaded, autoCoins=autoCoins, ch=ch)
    elif use_coin_purse(bagsLoaded):
        cname = "Coin Purse"
        purse = ch.coinpurse
        coins = {coin: purse[coin] for coin in COIN_TYPES}
        pouch = [cname, coins]
    else:
        pouch = get_bag(bagsLoaded, coinPouchName, exact_match=True, create_on_fail=True)
        for coin_type in COIN_TYPES:
            if coin_type not in pouch[1]:
                pouch[1][coin_type] = 0
    return pouch


def use_coin_purse(bagsLoaded: list) -> bool:
    """
    Checks if coin purse should be used.
    Returns a boolean
    :arg list bagsLoaded: The list of bags to check
    :return: a bool of whether to use the coin purse
    :rtype: bool
    """
    bagsLoaded = _as_list(bagsLoaded)
    return not get_bag(bagsLoaded, coinPouchName, exact_match=True) and COIN_RATES == DEFAULT_COIN_RATES


def parsecoins(args: str | list, coin_types=COIN_TYPES, default_coin=DEFAULT_COIN) -> (dict, bool):
    """
    Parses args to get the valid coins.
    :arg str|list args: the string or list of arguments to parse
    :var dict coin_types: the types of coins which are valid. Spaces in the names will parse multiple words to the same coin, eg "gp gold" will match `gp` or `gold` or `gp gold` default: self.COIN_TYPES
    :var str default_coin: the coin to use if none is given (won't match if an invalid coin in given) default: self.DEFAULT_COIN
    :return: tuple of a dict of coin deltas and an error bool
    :rtype: (dict, bool)
    """
    return parse_items(args, coin_types, default_coin)


def parse_items(args: str | list, types, default=None) -> (dict, bool):
    """
    Parses args to get the deltas of items given a list of valid items.
    :arg str|list args: the string or list of arguments to parse
    :arg dict types: the types of items which are valid. Spaces in the names will parse multiple words to the same item, eg "gp gold" will match `gp` or `gold` or `gp gold`
    :var str default: the item to use if none is given (won't match if an invalid item in given) default: None
    :return: tuple of a dict of item deltas and an error bool
    :rtype: (dict, bool)
    """
    if typeof(args) == 'SafeList':
        args = ' '.join(args)
    args = [arg.strip() for arg in args.split("+") if arg]
    new_args = []
    for arg in args:
        new_args += [f"{'-' if idx else ''}{part}" for idx, part in enumerate(arg.split("-")) if part]
    args = new_args
    items = {}
    for arg in args:
        if default in types and arg.replace("-", "").replace(",", "").replace(".", "", 1).strip().isdecimal():
            item = default
            arg = arg.strip()
        elif len(possible_types := ([item for item in types if arg.lower() == item.lower()] or [item for item in types if arg.lower() in item.lower() or item.lower() in arg.lower()])) == 1:
            item = possible_types[0]
            for part in item.lower().split():
                arg = arg.lower().replace(part, "").strip()
        else:
            return {}, True
        if all([number.strip().isdecimal() for number in (numbers := arg.strip("-").replace(",", "").split("."))]) and len(numbers) in (1, 2):
            quantity = float(arg.replace(",", ""))
            if quantity:
                items.update({item: items.get(item, 0)+quantity})
        else:
            return {}, True

    return items, False


def find_bag_with_item(bagsLoaded: list, item: str) -> a_bag:
    """
    Finds and returns the first bag with a given item in it.
    :arg list bagsLoaded: the list of bags to search in
    :arg str item: the desired item
    :return: the first bag with the desired item.
    :rtype: a_bag
    """
    possible_bags = []
    bagsLoaded = _as_list(bagsLoaded)
    for bag_name, items in bagsLoaded:
        if any([item.lower() == i.lower() for i in items]):
            return [bag_name, items]
        if any([item.lower() in i.lower() for i in items]):
            possible_bags.append([bag_name, items])
    return possible_bags[0] if possible_bags else None

def find_valid_name(a_dict: dict, input_str: str) -> str:
    """
    Finds a unique permutation for a key given a dict and a name.
    Also limits a bag's name to 200 characters to not overrun field name limits.
    :arg dict a_dict: the dict to search in
    :arg str input_str: the base name to check with
    :return: a similar string which is not used as a key
    :rtype: str
    """
    a_dict = _as_dict(a_dict)
    input_str = input_str[:200]
    i = int(input_str.split(' ')[-1]) if input_str.split(' ')[-1].isdecimal() else 1
    while input_str in a_dict:
        i += 1
        input_str = f"""{input_str.rstrip(" 1234567890")} {i}"""
    return input_str


def rename_bag(bagsLoaded: list, old_name: str, new_name: str) -> (str, str):
    """
    Renames a bag given the old name, and a new name.
    :arg list bagsLoaded: the list of bags to modify
    :arg str old_name: the current name of the bag
    :arg str new_name: the new name of the bag
    :return: a tuple of the old name and the new name as strings
    :rtype: (str, str)
    """
    bagsLoaded = _as_list(bagsLoaded)
    old_bag = get_bag(bagsLoaded, old_name)
    old_name = old_bag[0]
    if not old_bag:
        return (old_name, None)
    old_bag[0] = find_valid_name(bagsLoaded, new_name)
    return (old_name, old_bag[0])


def swap_pos(bagsLoaded: list, bag_name: str, position=1) -> (str, int):
    """
    Swaps the position of a bag in the display.
    :arg list bagsLoaded: the list of bags to modify
    :arg str bag_name: the name of the bag you want to move
    :var int position: the new position you want the bag in, indexed from 1 default: 1
    :return: a tuple of the name and the new position, or `(None, -1)` if the bag didn't exist
    :rtype: (str, int)
    """
    bag = get_bag(bagsLoaded, bag_name)
    if not bag:
        return None, -1
    bagsLoaded.remove([bag[0], bag[1]])
    position = max(min(len(bagsLoaded), position), 1)
    bagsLoaded.insert(position-1, bag)
    return bag[0], position


def delete_bag(bagsLoaded: list, bag_name: str) -> (str, bool):
    """
    Deletes the bag with the given name.
    :arg list bagsLoaded: the list to remove the bag from
    :arg str bag_name: the name of the bag to remove, exact match required
    :return: the name of the bag attemped to be deleted, and a bool of whether it was successful
    :rtype: (str, bool)
    """
    bagsLoaded = _as_list(bagsLoaded)
    old_bag = get_bag(bagsLoaded, bag_name, exact_match=True)
    if not old_bag:
        return (bag_name, True)
    bagsLoaded.remove(old_bag)
    return (old_bag[0], False)


def set_custom_weight(item_name: str, weight: float = None, cost: str = None, bundle: int = None, ch=character()) -> bool:
    """
    Adds a custom weight to the custWeights cvar.
    :arg str item_name: the name of the item you want to configure
    :var float weight: the weight of the item represented as a float or int default: None
    :var str cost: the cost of the item, represented as <number><denomination> eg "1gp" for 1 gold piece default: None
    :var int bundle: how many items in a bundle, this is the grouping you have to buy these items in default: None
    :var ch: your character default: character()
    :return: a boolean representing the success of the modification
    :rtype: bool
    """
    # build item config dict
    item = (custWeights.get(item_name) or custWeights.get(item_name.lower(), {})) | {x: y for x, y in [('weight', weight), ('cost', cost), ('bundle', bundle)] if y is not None}
    success = False
    if item:
        custWeights.update({item_name.lower(): item})
        weightDict.update({item_name.lower(): item})
        success = True
        ch.set_cvar('bagSettings', dump_json(settings))
    return success

def get_item_weight(item: str, fuzzy_item_count: int = 0, weightDict: dict = weightDict) -> (float | str, int, bool):
    """
    Grabs the weight of the given item.
    Also allows keeping track of how many items have used a fuzzy search, which is more intensive.
    :arg str item: the name of the item
    :var int fuzzy_item_count: the current count of how many fuzzy matches have been made default: 0
    :var dict weightDict: the dict to pull weights from default: self.weightDict
    :return: the weigh, the total number of fuzzy items, and whether no matching weight was found.
    :rtype: (float|str, int, bool)
    """
    item_name = item.lower()
    unknownItem = False
    if item_name in weightDict and ((typeof(dict_entry := weightDict[item_name]) != "SafeDict") or 'weight' in dict_entry):
        itemWeight = (dict_entry if typeof(dict_entry) != "SafeDict" else dict_entry['weight'])
    elif item_name in COIN_TYPES:
        itemWeight = coinWeighs
    elif "pouch" in item_name:
        itemWeight = 1
    elif "potion" in item_name:
        itemWeight = 0.5
    elif fuzzy_item_count < 5:
        fuzzy_item_count += 1
        itemWeight = ([(v.get("weight") if typeof(v) == "SafeDict" else v) for k, v in weightDict.items() if k in item_name and (typeof(v) != "SafeDict" or 'weight' in v)]+["†"])[0]
    else:
        itemWeight = "†"
        unknownItem = True

    return itemWeight, fuzzy_item_count, unknownItem


def weigh_bag(
    bag: a_bag,
    weightDict: dict = weightDict,
    weightTracking: bool = (settings.get('weightTracking', 'Off').lower() == 'on'),
    ignoreBags: list = settings.get('weightlessBags', ["bag of holding", "handy haversack", "heward's handy haversack"])
) -> (float, float, int):
    """
    Returns a tuple of values relevant to the weighing of a bag.
    :arg a_bag bag: the bag to get the weight of
    :var dict weightDict: the dict to pull weights from default: self.weightDict
    :var bool weightTracking: whether to track weight default: self.settings.weightTracking
    :var list ignoreBags: the list of lowercase bag name to skip weight tracking for default: self.settings.weightlessBags
    :return: the total and coin weight in lbs, and the total number of fuzzy matches
    :rtype: (float, float, int)
    """
    # define variables
    total_weight = 0
    coin_weight = 0
    total_fuzzy_count = 0

    # loop over all the items in the bag, getting the necessary information for each
    for item in bag[1]:
        if weightTracking and bag[0].lower() not in ignoreBags:
            item_name = item.lower()
            itemWeight, fuzzy_count, _ = get_item_weight(item, total_fuzzy_count, weightDict)
            total_fuzzy_count += fuzzy_count

            itemWeight = itemWeight*(bag[1][item] if typeof(itemWeight) != 'str' else 1)

            if typeof(itemWeight) != 'str':
                total_weight += itemWeight
                if item_name in COIN_TYPES:
                    coin_weight += itemWeight

    return float(total_weight), float(coin_weight), total_fuzzy_count


def display_bag(
    bag: a_bag,
    weightDict: dict = weightDict,
    weightTracking: bool = (settings.get('weightTracking', 'Off').lower() == 'on'),
    ignoreBags: list = settings.get('weightlessBags', ["bag of holding", "handy haversack", "heward's handy haversack"]),
    old_bag: dict = None,
    length_limiter: str = settings.get('handleLongNames', 'newrow')
) -> (list, float, float, int, bool):
    """
    Creates the field(s) to display a bag in an embed.
    :arg a_bag bag: the bag to get the weight of
    :var dict weightDict: the dict to get weights from default: self.weightDict
    :var bool weightTracking: whether to use weight tracking default: self.settings.weightTracking
    :var list ignoreBags: a list of what bags are ignored default: self.settings.weightlessBags
    :var dict old_bag: the bag's contents previous state, for building a delta from default: None
    :var str length_limiter: how to limit the length of a long line. default: self.settings.handleLongNames
    :return: a list of fields to display a bag, the total weight of the bag, the weight of the coins, the total number of fuzzy matches, as well as a bool of whether any items had no matches
    :rtype: (list, float, float, int, bool)
    """

    # define variables
    item_messages = []
    total_weight = 0
    coin_weight = 0
    fuzzy_item_count = 0
    anyUnknownItem = False

    # loop over each item, getting the information needed for the display
    for item in bag[1]:
        item_name = item.lower()
        quantity = bag[1][item]

        item_message = f"{ITEM_PREFIXES[item_name]} " if item_name in ITEM_PREFIXES else ""
        item_message += f"""{quantity:,}{"" if item_name in COIN_TYPES else "x"} {item}""".strip()

        # get item amount differences
        if old_bag is not None:
            diff = quantity - old_bag.get(item, 0)
            if diff:
                item_message += f''' ({"+" if diff>0 else ""}{diff})'''

        # start weight calculation
        if weightTracking and bag[0].lower() not in ignoreBags:  # only weigh the bag if it's enabled
            itemWeight, fuzzy_item_count, unknownItem = get_item_weight(item, fuzzy_item_count, weightDict)
            anyUnknownItem = anyUnknownItem or unknownItem

            itemWeight = itemWeight*(quantity if typeof(itemWeight) != 'str' else 1)

            if typeof(itemWeight) != 'str':
                total_weight += itemWeight
                if item_name in COIN_TYPES:
                    coin_weight += itemWeight

            # add the correct message based on the weight
            if itemWeight and typeof(itemWeight) in ['int', 'float']:
                item_message += f''' [{round_nicely(itemWeight)} lbs.]{asterisk if unknownItem else ""}'''
            else:
                item_message += f" {itemWeight}" if itemWeight else ""

        item_messages.append(item_message)

    if old_bag is not None:
        for item in old_bag:
            if item not in bag[1]:
                item_messages.append(f"0x {item} (-{old_bag[item]})")

    # show empty message
    if not item_messages:
        item_messages = ['*This bag is empty.*']

    # add weight counter for coins and total for each bag
    if coin_weight:
        item_messages.append(f"""**Coin Weight:** {round_nicely(coin_weight)} lbs.""")
    bag_title = f"""{bag[0]}{"†" if anyUnknownItem else f''' ({round_nicely(total_weight)} lbs.)''' if total_weight else ""}"""

    # split up fields if they are too long
    fields = []
    i = 0
    while item_messages:
        header = bag_title if i == 0 else f"{bag[0]} *(continued)*"
        lineLength = len(header)
        item_message = item_messages.pop(0)
        max_length = 35
        if any(emojis := [emoji for emoji in DEFAULT_COIN_EMOJIS.values() if emoji in item_message]):
            max_length += len(''.join(emojis)) - 2*len(emojis)
        if length_limiter == 'truncate':
            if len(item_message) > max_length:
                item_message = item_message[:max_length-3]+"..."
        fields.append(f"-f ＂{header}|{item_message}")
        lineLength = max(lineLength, len(item_message))
        while item_messages:
            max_length = 35
            item_message = item_messages[0]
            if any(emojis := [emoji for emoji in DEFAULT_COIN_EMOJIS.values() if emoji in item_message]):
                max_length += len(''.join(emojis)) - 2*len(emojis)
            if length_limiter == 'truncate':
                if len(item_message) > max_length:
                    item_message = item_message[:max_length-3]+"..."
            if (len(fields[i]) + len(item_message) + 1) <= 1024:
                item_messages.pop(0)
                fields[i] += f"\n{item_message}"
                lineLength = max(lineLength, len(item_message))
            else:
                break
        fields[i] += "|inline＂" if length_limiter in ['newline', 'truncate'] or lineLength <= max_length else "＂"
        i += 1

    return fields, float(total_weight), float(coin_weight), fuzzy_item_count, anyUnknownItem


def display_coins(
    bagsLoaded: list,
    compact: bool = settings.get('compactCoins', get("compactcoins", "0") == "1"),
    old_coins: dict = None
) -> list:
    """
    Creates the field(s) to display coins in an embed.
    :arg list bagsLoaded: the loaded list of bags
    :var bool compact: whether to use compact view default: self.settings.compactCoins
    :var dict old_coins: the old coins for comparing to default: None
    :return: a list of fields to display coins
    :rtype: list
    """

    # define variables
    bagsLoaded = _as_list(bagsLoaded)
    bag = get_coins(bagsLoaded)
    item_messages = []
    old_total = None
    coin_total = None
    if compact:
        old_total = sum(old_coins[coin]/COIN_RATES[coin] for coin in COIN_TYPES if coin.lower() in old_coins) if old_coins else None
        coin_total = sum(bag[1][coin]/COIN_RATES[coin] for coin in COIN_TYPES if coin.lower() in bag[1]) if bag[1] else 0.0

    # loop over each item, getting the information needed for the display
    for item in bag[1]:
        item_name = item.lower()

        if compact and item_name in COIN_TYPES:
            continue

        quantity = bag[1][item]
        if item_name in ITEM_PREFIXES:
            item_message = f"""{ITEM_PREFIXES[item_name]} {quantity:,}{"" if item_name in COIN_TYPES else "x"} {item}""".strip()
        else:
            item_message = f"""{quantity:,}{"" if item_name in COIN_TYPES else "x"} {item}""".strip()

        # get item amount differences
        if old_coins is not None:
            diff = quantity - old_coins.get(item, 0)
            if diff:
                item_message += f''' ({"+" if diff>0 else ""}{round_nicely(diff)})'''

        item_messages.append(item_message)

    # add total coin entry
    if compact:
        prefix = ITEM_PREFIXES.get(DEFAULT_COIN)
        item_message = f"""{prefix + " " if prefix else ""}Total Value: {round_nicely(coin_total)} {DEFAULT_COIN}""".strip()
        if old_total is not None:
            diff = coin_total - old_total
            if diff:
                item_message += f''' ({"+" if diff>0 else ""}{round_nicely(diff)})'''
        item_messages.append(item_message)

    # show empty message
    if not item_messages:
        item_messages = ['*This bag is empty.*']

    # add weight counter for coins and total for each bag
    bag_title = f"""{bag[0]}"""

    # split up fields if they are too long
    fields = []
    i = 0
    while item_messages:
        header = bag_title if i == 0 else "*(continued)*"
        lineLength = len(header)
        item_message = item_messages.pop(0)
        fields.append(f"-f ＂{header}|{item_message}")
        lineLength = max(lineLength, len(item_message))
        while len(fields[i]) <= 1000:
            if not item_messages:
                break
            item_message = item_messages.pop(0)
            fields[i] += f"\n{item_message}"
            lineLength = max(lineLength, len(item_message))
        fields[i] += "＂"
        i += 1

    return fields


def create_display(
    bagsLoaded: list = [],
    focus: a_bag = None,
    openMode: str = settings.get('openMode', 'All'),
    old_bags: dict = {},
    weightDict: dict = weightDict,
) -> list:
    """
    Creates the full display for a list of bags.
    If a focus is provided but bagsLoaded is not, displays focus instead.
    :var list bagsLoaded: the list of bags to display for the 'All' mode default: []
    :var a_bag focus: a bag to focus on for the 'One' mode default: None
    :var str openMode: an override to the open mode default: self.settings.openMode
    :var dict old_bags: a copy of bagsLoaded made before any changes were made, used for item diffs. Make sure the copy is deep by running baglib.deep_copy(bagsLoaded) default: {}
    :return: a list of embed arguments to display the list of bags
    :rtype: list
    """
    # define variables
    openMode = openMode.lower() if openMode and openMode.lower() in openModes else settings.get('openMode', 'All').lower()
    text = []
    weightTracking = settings.get('weightTracking', 'Off').lower() == 'on'
    ignoreBags = settings.get('weightlessBags', ["bag of holding", "handy haversack", "heward's handy haversack"])
    old_bags = _as_dict(old_bags)

    # define loop based on what mode we're in
    match openMode:
        case 'none':
            loop = []
        case 'all':
            bagsLoaded = _as_list(bagsLoaded)
            loop = bagsLoaded + ([get_coins(bagsLoaded)] if use_coin_purse(bagsLoaded) else [])
        case _:
            loop = [focus] if focus else []

    if not loop:
        return ["-desc ＂There are no bags to display.＂"]
    else:
        carriedWeight = 0
        unknownTotal = 0
        anyUnknownItem = False

        # loop over the bags
        for bag in loop:
            if not bag:
                continue
            old_bag = None if old_bags is None else old_bags.get(bag[0], {})
            fields, bag_weight, _, fuzzy_item_count, UnknownItems = display_bag(bag, weightDict, weightTracking, ignoreBags, old_bag)
            text += fields
            anyUnknownItem = anyUnknownItem or UnknownItems
            carriedWeight += bag_weight
            unknownTotal += fuzzy_item_count
        # add footnotes based on weight results
        if weightTracking and openMode == 'all':
            display_footer = f'''-f ＂Total Weight Carried: {round_nicely(carriedWeight)}{asterisk*(unknownTotal>0)} lbs.|Carrying Capacity: {carryMod*15} lbs.'''
            if anyUnknownItem:
                display_footer += "\n*Items marked with a dagger (†) are entirely unrecognized.*"
            if unknownTotal:
                display_footer += f"""\n{asterisk+f"You have {unknownTotal} item{'s'*(unknownTotal>1)} which {doesntdont[unknownTotal>1]} have an exact match in the database."}"""
            display_footer += "＂"

            text.append(display_footer)

        # show encumbrance footer even if 'all' mode is not selected
        if weightTracking and settings.get('encumbrance', 'Off').lower() == 'on':
            if openMode not in 'all':
                carriedWeight = carried_weight(bagsLoaded)
            encumbrance_footer = """\n -f ＂You are Heavily Encumbered| Your speed is reduced by 20 feet and you have disadvantage on ability checks, attack rolls, and saving throws that use Strength, Dexterity, or Constitution.＂""" if carriedWeight > (carryMod*10) else """ -f ＂You are Encumbered|Your speed is reduced by 10 feet.＂""" if carriedWeight > (carryMod*5) else ""
            text.append(encumbrance_footer)
    return text


def carried_weight(bagsLoaded: list) -> float:
    """
    Calculates the total weight of a list of bags.
    :arg list bagsLoaded: the list of bags
    :return: a float representing the total weight
    :rtype: float
    """
    bagsLoaded = _as_list(bagsLoaded)
    coinbag = [get_coins(bagsLoaded)]
    loop = bagsLoaded + coinbag if coinbag not in bagsLoaded else []
    carriedWeight = 0

    for bag in loop:
        bag_weight, _, _ = weigh_bag(bag, weightDict, 'on')
        carriedWeight += bag_weight
    return float(carriedWeight)


def save_state(bagsLoaded: list) -> list:
    """
    Returns a copy of bags that won't be modified.
    Useful for old_bags in create_display
    :arg list bagsLoaded: the list of bags
    :return: a copy of bagsLoaded, plus the coin pouch if appropriate
    :rtype: list
    """
    return _deep_copy(bagsLoaded) + ([get_coins(bagsLoaded)] if use_coin_purse(bagsLoaded) else [])


def _deep_copy(obj):
    """
    Provides a deep copy of an object.
    :arg T obj: anything
    :return: a deep copy of obj
    :rtype: T
    """
    return load_yaml(dump_yaml(obj))


def _as_dict(listordict) -> dict:
    """
    Makes sure a list is returned as a dict
    :var list|dict listordict: The list or dict to check
    :return: a dict
    :rtype: dict
    """
    match typeof(listordict):
        case 'SafeDict':
            return listordict
        case 'SafeList' if len(listordict) == 0 or len(max(listordict, key=len)) == 2:
            return dict(listordict)
        case _:
            err(f"{typeof(listordict)} cannot be converted to a dict.\n{listordict} caused this error.", True)


def _as_list(listordict) -> list:
    """
    Makes sure a dict is returned as a list of lists
    :var list|dict listordict: The list or dict to check
    :return: a list
    :rtype: list
    """
    match typeof(listordict):
        case 'SafeDict':
            return list(listordict.items())
        case 'SafeList':
            return listordict
        case _:
            err(f"{typeof(listordict)} cannot be converted to a list.\n{listordict} caused this error.", True)


def round_nicely(number: int | float) -> str:
    """
    Makes the number look nice, regardless of whether it's an int or a float
    :arg int|float number: an integer or float
    :return: the rounded number as a string
    :rtype: str
    """
    return f'{number:,.2f}'.rstrip('0').rstrip('.').replace(",", " ")


def _get_ratio(a: int | float | str, b: int | float | str) -> (int, int):
    """
    Determines the simplest integer ratio between a and b.
    Calculate the Greatest Common Divisor of a and b. Also returns the decimal adjustment used to avoid floating point errors.
    Best used on floating points less than 2 decimals long. Fractions as strings are also supported, eg. '2/3' or '1/7'.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).

    :arg int|float a: a number
    :arg int|float b: another number
    :return: a pair of numbers that is the reduced ratio
    :rtype: (int, int)
    """
    match (typeof(a), typeof(b)):
        case ('str', 'str'):
            a_pair = [int(x) for x in a.split('/') if x.isdecimal()][:2]
            while len(a_pair) < 2:
                a_pair.append(1)
            b_pair = [int(x) for x in b.split('/') if x.isdecimal()][:2]
            while len(b_pair) < 2:
                b_pair.append(1)
            a = a_pair[0]*b_pair[1]
            b = a_pair[1]*b_pair[0]
        case ('str', _):
            a_pair = [int(x) for x in a.split('/') if x.isdecimal()][:2]
            while len(a_pair) < 2:
                a_pair.append(1)
            a = a_pair[0]*b
            b *= a_pair[1]
        case (_, 'str'):
            b_pair = [int(x) for x in b.split('/') if x.isdecimal()][:2]
            while len(b_pair) < 2:
                b_pair.append(1)
            b = b_pair[0]*a
            a *= b_pair[1]
    decimal = 1
    a1 = a
    b1 = b
    while a1 % 1 or b1 % 1:
        a1 *= 10
        b1 *= 10
        decimal *= 10
    while b1:
        a1, b1 = b1, a1 % b1
    return int(a*decimal//a1), int(b*decimal//a1)