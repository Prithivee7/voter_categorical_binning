def perform_binning_political_parties(party_name: str) -> str:
    """
    Categorises the political parties.
    The parties are DEM(DEMOCRATIC), LIB(LIBERTARIAN), REP(REPUBLICAN), UNA(UNAFFILIATED) and GRE
    They are binned into DEM, REP and others


    Args:
        party_name (str): Name of the party.

    Returns:
        str: The category of the party.

    Examples:
        >>> perform_binning_political_parties('REP')
        'Republican'

    """
    if party_name == "REP":
        return "Republican"
    elif party_name == "DEM":
        return "Democratic"
    else:
        return "Others"


def perform_binning_races(race_name: str) -> str:
    """
    Categorises the Races.
    The available races are A(ASIAN), B(BLACK or AFRICAN AMERICAN), I(INDIAN AMERICAN or ALASKA NATIVE)
    M(TWO or MORE RACES), O(OTHER), U(UNDESIGNATED), W(WHITE), P, UN
    White, Black, Asian and Indian American are kept as separate categories while the rest are grouped into Others


    Args:
        race_name (str): Name of the Race.

    Returns:
        str: The category of the race.

    Examples:
        >>> perform_binning_races('B')
        'Black'

    """
    if race_name == "W":
        return "White"
    elif race_name == "B":
        return "Black"
    elif race_name == "A":
        return "Asian"
    elif race_name == "I":
        return "Indian American"
    else:
        return "Others"


def get_age_bracket(age_bracket: str) -> str:
    """
    Get the age feature.

    Args:
        age_bracket (str): The age bracket.

    Returns:
        str: age_bracket

    Examples:
        >>> get_age_bracket('Age 18 - 25')
        'Age 18 - 25'

    """
    if age_bracket == 1:
        return "NA"
    else:
        return age_bracket


def perform_binning_sex(sex_of_individual: str) -> str:
    """
    Categorises the Sex of the voters.
    The voters are classified into M(Male), F(Female) and Others

    Args:
        sex_of_individual (str): Sex of the voter.

    Returns:
        str: Sex of the voter.

    Examples:
        >>> perform_binning_sex('F')
        'Female'

    """
    if sex_of_individual == "F":
        return "Female"
    elif sex_of_individual == "M":
        return "Male"
    else:
        return "Others"


def perform_binning_ethnicity(ethnicity_name: str) -> str:
    """
    Categorises the Ethnicity of the voters.
    The available ethicities are HL(HISPANIC or LATINO), NL(NOT HISPANIC or NOT LATINO)
    UN(UNDESIGNATED). Based on this they are classified into HL, NL and Others 

    Args:
        ethnicity_name (str): Ethnicity of the voter.

    Returns:
        str: Ethnicity of the voter.

    Examples:
        >>> perform_binning_ethnicity('HL')
        'Hispanic or Latino'

    """
    if ethnicity_name == "HL":
        return "Hispanic or Latino"
    elif ethnicity_name == "NL":
        return "NOT HISPANIC or NOT LATINO"
    else:
        "Others"


def get_county_id(county_name: str) -> str:
    """
    Gets the County ID based on the County Name.
    This information can be found here -> https://s3.amazonaws.com/dl.ncsbe.gov/data/layout_ncvoter.txt

    Args:
        county_name (str): Name of the county.

    Returns:
        str: County ID.

    Examples:
        >>> get_county_id('ALEXANDER')
        '2'

    """
    county_name_id_mapping = {
        "ALAMANCE":        1,
        "ALEXANDER":        2,
        "ALLEGHANY":        3,
        "ANSON":        4,
        "ASHE":        5,
        "AVERY":        6,
        "BEAUFORT":        7,
        "BERTIE":        8,
        "BLADEN":        9,
        "BRUNSWICK":       10,
        "BUNCOMBE":       11,
        "BURKE":       12,
        "CABARRUS":       13,
        "CALDWELL":       14,
        "CAMDEN":       15,
        "CARTERET":       16,
        "CASWELL":       17,
        "CATAWBA":       18,
        "CHATHAM":       19,
        "CHEROKEE":       20,
        "CHOWAN":       21,
        "CLAY":       22,
        "CLEVELAND":       23,
        "COLUMBUS":       24,
        "CRAVEN":       25,
        "CUMBERLAND":       26,
        "CURRITUCK":       27,
        "DARE":       28,
        "DAVIDSON":       29,
        "DAVIE":       30,
        "DUPLIN":       31,
        "DURHAM":       32,
        "EDGECOMBE":       33,
        "FORSYTH":       34,
        "FRANKLIN":       35,
        "GASTON":       36,
        "GATES":       37,
        "GRAHAM":       38,
        "GRANVILLE":       39,
        "GREENE":       40,
        "GUILFORD":       41,
        "HALIFAX":       42,
        "HARNETT":       43,
        "HAYWOOD":       44,
        "HENDERSON":       45,
        "HERTFORD":       46,
        "HOKE":       47,
        "HYDE":       48,
        "IREDELL":       49,
        "JACKSON":       50,
        "JOHNSTON":       51,
        "JONES":       52,
        "LEE":       53,
        "LENOIR":       54,
        "LINCOLN":       55,
        "MACON":       56,
        "MADISON":       57,
        "MARTIN":       58,
        "MCDOWELL":       59,
        "MECKLENBURG":       60,
        "MITCHELL":       61,
        "MONTGOMERY":       62,
        "MOORE":       63,
        "NASH":       64,
        "NEWHANOVER":       65,
        "NORTHAMPTON":       66,
        "ONSLOW":       67,
        "ORANGE":       68,
        "PAMLICO":       69,
        "PASQUOTANK":       70,
        "PENDER":       71,
        "PERQUIMANS":       72,
        "PERSON":       73,
        "PITT":       74,
        "POLK":       75,
        "RANDOLPH":       76,
        "RICHMOND":       77,
        "ROBESON":       78,
        "ROCKINGHAM":       79,
        "ROWAN":       80,
        "RUTHERFORD":       81,
        "SAMPSON":       82,
        "SCOTLAND":       83,
        "STANLY":       84,
        "STOKES":       85,
        "SURRY":       86,
        "SWAIN":       87,
        "TRANSYLVANIA":       88,
        "TYRRELL":       89,
        "UNION":       90,
        "VANCE":       91,
        "WAKE":       92,
        "WARREN":       93,
        "WASHINGTON":       94,
        "WATAUGA":       95,
        "WAYNE":       96,
        "WILKES":       97,
        "WILSON":       98,
        "YADKIN":       99,
        "YANCEY":       00
    }

    if county_name not in county_name_id_mapping:
        return "NA"
    else:
        return str(county_name_id_mapping[county_name])
