"""
Python model "final.py"
Translated using PySD version 0.10.0
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions

_subscript_dict = {}

_namespace = {
    'TIME': 'time',
    'Time': 'time',
    'Lithium demand': 'lithium_demand',
    'Exchange rate': 'exchange_rate',
    'normalised currency value in dollars': 'normalised_currency_value_in_dollars',
    '"2010 GDP"': '_gdp',
    'normalised public approval rate': 'normalised_public_approval_rate',
    'normalised unemployment percentage': 'normalised_unemployment_percentage',
    'normalised wealth fund': 'normalised_wealth_fund',
    'Threshold value world lithium demand': 'threshold_value_world_lithium_demand',
    'Decreasing investments': 'decreasing_investments',
    '"Account surplus/deficit"': 'account_surplusdeficit',
    'Depreciation': 'depreciation',
    'Increasing investments': 'increasing_investments',
    'Appreciation': 'appreciation',
    'normalised debt as percentage of GDP': 'normalised_debt_as_percentage_of_gdp',
    'Bubble perception factor': 'bubble_perception_factor',
    'Buying': 'buying',
    'Resulting investments': 'resulting_investments',
    'Initial LCU in foreign hands': 'initial_lcu_in_foreign_hands',
    'Selling': 'selling',
    'Currency speculation': 'currency_speculation',
    'Market LCU pricing': 'market_lcu_pricing',
    'Tradeable LCU in foreign hands': 'tradeable_lcu_in_foreign_hands',
    'Total imports AGR IND SERV in LCU': 'total_imports_agr_ind_serv_in_lcu',
    'Initial currency speculation': 'initial_currency_speculation',
    'Normalised currency speculation sell': 'normalised_currency_speculation_sell',
    'Reserved for investments': 'reserved_for_investments',
    'LCU in the market': 'lcu_in_the_market',
    'Initial LCU in market': 'initial_lcu_in_market',
    'national unemployment previous year': 'national_unemployment_previous_year',
    'Debt': 'debt',
    'local unemployment': 'local_unemployment',
    'public approval rate': 'public_approval_rate',
    'HDI previous year': 'hdi_previous_year',
    'decreasing popularity': 'decreasing_popularity',
    'national unemployment percentage': 'national_unemployment_percentage',
    'increasing popularity': 'increasing_popularity',
    'Lithium exports in LCU': 'lithium_exports_in_lcu',
    'Currency value in dollars': 'currency_value_in_dollars',
    'Foreign demand AGR IND SERV in LCU': 'foreign_demand_agr_ind_serv_in_lcu',
    'GDP in real terms': 'gdp_in_real_terms',
    'Foreign investments in LCU': 'foreign_investments_in_lcu',
    'Total exports AGR IND SERV in LCU': 'total_exports_agr_ind_serv_in_lcu',
    'GDP': 'gdp',
    'Tax income in dollars': 'tax_income_in_dollars',
    '"Surplus/Deficit"': 'surplusdeficit',
    '"2010 foreign demand AGR IND SERV in dollars"': '_foreign_demand_agr_ind_serv_in_dollars',
    '"2010 foreign investment"': '_foreign_investment',
    '"2010 imports in dollars"': '_imports_in_dollars',
    'Interest payments': 'interest_payments',
    'Interest rate': 'interest_rate',
    'Foreign investments in dollars': 'foreign_investments_in_dollars',
    '"2014 debt as percentage of GDP"': '_debt_as_percentage_of_gdp',
    'Domestic demand for AGR IND SERV': 'domestic_demand_for_agr_ind_serv',
    'GDP per capita in LCU': 'gdp_per_capita_in_lcu',
    'Lithium exports in dollars': 'lithium_exports_in_dollars',
    'Government expenditure': 'government_expenditure',
    'Government income': 'government_income',
    'Debt as percentage of GDP': 'debt_as_percentage_of_gdp',
    'decommissioning': 'decommissioning',
    'Decommissioning delay': 'decommissioning_delay',
    'new production capacity': 'new_production_capacity',
    'Domestic production capacity AGR IND SERV': 'domestic_production_capacity_agr_ind_serv',
    'income index': 'income_index',
    'Init domestic production capacity': 'init_domestic_production_capacity',
    'New production capacity delay': 'new_production_capacity_delay',
    'Total exports': 'total_exports',
    '"Production capacity surplus/deficit"': 'production_capacity_surplusdeficit',
    '"Fraction GDP/consumer consumption"': 'fraction_gdpconsumer_consumption',
    'Gross National Income per capita': 'gross_national_income_per_capita',
    'Taxation rate': 'taxation_rate',
    '"2010 Life expectancy"': '_life_expectancy',
    '"2010 Lithium production"': '_lithium_production',
    '"2010 MYS"': '_mys',
    'Investment in wealth fund': 'investment_in_wealth_fund',
    'Amortising': 'amortising',
    'Wealth fund': 'wealth_fund',
    'Borrowing': 'borrowing',
    'Life expectancy': 'life_expectancy',
    'Life Expectancy Index': 'life_expectancy_index',
    'mean years of schooling index': 'mean_years_of_schooling_index',
    'Mean years of schooling': 'mean_years_of_schooling',
    'Education Fraction': 'education_fraction',
    'Health Fraction': 'health_fraction',
    'Saving': 'saving',
    'Human Development spending': 'human_development_spending',
    'Education expenditure': 'education_expenditure',
    'New HD spending': 'new_hd_spending',
    'Productivity mining sector': 'productivity_mining_sector',
    'Social spending': 'social_spending',
    'Health expenditure': 'health_expenditure',
    'agriculture water use': 'agriculture_water_use',
    'natural replenishing': 'natural_replenishing',
    'government agriculture research investment factor':
    'government_agriculture_research_investment_factor',
    'labour demand': 'labour_demand',
    'Labour participation rate in 2019': 'labour_participation_rate_in_2019',
    'People working in mining sector in 2017': 'people_working_in_mining_sector_in_2017',
    'migration out': 'migration_out',
    'Per capita water use': 'per_capita_water_use',
    'Replenishing': 'replenishing',
    'water use': 'water_use',
    'water required per metric ton of lithium mined':
    'water_required_per_metric_ton_of_lithium_mined',
    'industry water use': 'industry_water_use',
    'migration in': 'migration_in',
    'water efficiency of agriculture': 'water_efficiency_of_agriculture',
    '"Over-use"': 'overuse',
    'Water stress': 'water_stress',
    'water stocks': 'water_stocks',
    'change in EYS': 'change_in_eys',
    'chilean lithium in use globally': 'chilean_lithium_in_use_globally',
    'corporate income from lithium mining': 'corporate_income_from_lithium_mining',
    'LCE demand': 'lce_demand',
    'domestic water use': 'domestic_water_use',
    'Edu system delay': 'edu_system_delay',
    'Education index': 'education_index',
    'efficiency factor': 'efficiency_factor',
    'Expected Years of Schooling': 'expected_years_of_schooling',
    'expected years of schooling index': 'expected_years_of_schooling_index',
    'fraction of population dependent on mining sector':
    'fraction_of_population_dependent_on_mining_sector',
    'fraction of population dependent on other sectors':
    'fraction_of_population_dependent_on_other_sectors',
    'global market price per metric ton': 'global_market_price_per_metric_ton',
    'government income from lithium mining': 'government_income_from_lithium_mining',
    'government mining research investment factor': 'government_mining_research_investment_factor',
    'Health system delay': 'health_system_delay',
    'Human Development Index': 'human_development_index',
    'initial EYS': 'initial_eys',
    'initial identified reserves': 'initial_identified_reserves',
    'initial local population': 'initial_local_population',
    'initial population': 'initial_population',
    'lithium salt reserves': 'lithium_salt_reserves',
    'local population': 'local_population',
    'loss': 'loss',
    'mining expertise': 'mining_expertise',
    'mining water use': 'mining_water_use',
    'Money per year of extra education': 'money_per_year_of_extra_education',
    'Money per year of extra living': 'money_per_year_of_extra_living',
    'nationalisation SWITCH': 'nationalisation_switch',
    'net population growth': 'net_population_growth',
    'production': 'production',
    'Taxation': 'taxation',
    'Total population Chile': 'total_population_chile',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'TIME STEP': 'time_step'
}

__pysd_version__ = "0.10.0"

__data = {'scope': None, 'time': lambda: 0}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


def time():
    return __data['time']()


@cache('step')
def lithium_demand():
    """
    Real Name: b'Lithium demand'
    Original Eqn: b'WITH LOOKUP ( Time, ([(0,0)-(40,400000)],(0,40890),(1,48250),(2,55900),(3,47600),(4,49390),(5,49610),(6\\\\ ,65160),(10,100000),(15,150000),(20,397400),(23,371900),(26,21050),(29,23680),(31,39470\\\\ ),(33,21050),(40,20000) ))'
    Units: b'metric ton/year'
    Limits: (None, None)
    Type: component

    b'Li2CO3 equivalent'
    """
    return functions.lookup(time(), [0, 1, 2, 3, 4, 5, 6, 10, 15, 20, 23, 26, 29, 31, 33, 40], [
        40890, 48250, 55900, 47600, 49390, 49610, 65160, 100000, 150000, 397400, 371900, 21050,
        23680, 39470, 21050, 20000
    ])


@cache('step')
def exchange_rate():
    """
    Real Name: b'Exchange rate'
    Original Eqn: b'(Tradeable LCU in foreign hands+Reserved for investments)/LCU in the market'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (tradeable_lcu_in_foreign_hands() + reserved_for_investments()) / lcu_in_the_market()


@cache('step')
def normalised_currency_value_in_dollars():
    """
    Real Name: b'normalised currency value in dollars'
    Original Eqn: b'Currency value in dollars'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return currency_value_in_dollars()


@cache('run')
def _gdp():
    """
    Real Name: b'"2010 GDP"'
    Original Eqn: b'2.185e+11'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 2.185e+11


@cache('step')
def normalised_public_approval_rate():
    """
    Real Name: b'normalised public approval rate'
    Original Eqn: b'public approval rate/50'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return public_approval_rate() / 50


@cache('step')
def normalised_unemployment_percentage():
    """
    Real Name: b'normalised unemployment percentage'
    Original Eqn: b'national unemployment percentage/0.35'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return national_unemployment_percentage() / 0.35


@cache('step')
def normalised_wealth_fund():
    """
    Real Name: b'normalised wealth fund'
    Original Eqn: b'Wealth fund'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return wealth_fund()


@cache('run')
def threshold_value_world_lithium_demand():
    """
    Real Name: b'Threshold value world lithium demand'
    Original Eqn: b'80000'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 80000


@cache('step')
def decreasing_investments():
    """
    Real Name: b'Decreasing investments'
    Original Eqn: b'MAX(0,Reserved for investments-Resulting investments)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(0, reserved_for_investments() - resulting_investments())


@cache('step')
def account_surplusdeficit():
    """
    Real Name: b'"Account surplus/deficit"'
    Original Eqn: b'(Total exports AGR IND SERV in LCU-Total imports AGR IND SERV in LCU)*Exchange rate +Lithium exports in dollars +Foreign investments in dollars'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return (total_exports_agr_ind_serv_in_lcu() - total_imports_agr_ind_serv_in_lcu()
            ) * exchange_rate() + lithium_exports_in_dollars() + foreign_investments_in_dollars()


@cache('step')
def depreciation():
    """
    Real Name: b'Depreciation'
    Original Eqn: b'MAX(0, (Threshold value world lithium demand-Lithium demand)*Bubble perception factor\\\\ )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(0, (threshold_value_world_lithium_demand() - lithium_demand()) *
                      bubble_perception_factor())


@cache('step')
def increasing_investments():
    """
    Real Name: b'Increasing investments'
    Original Eqn: b'MAX(0,Resulting investments-Reserved for investments)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(0, resulting_investments() - reserved_for_investments())


@cache('step')
def appreciation():
    """
    Real Name: b'Appreciation'
    Original Eqn: b'MAX(0, (Lithium demand-Threshold value world lithium demand))'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(0, (lithium_demand() - threshold_value_world_lithium_demand()))


@cache('step')
def normalised_debt_as_percentage_of_gdp():
    """
    Real Name: b'normalised debt as percentage of GDP'
    Original Eqn: b'Debt as percentage of GDP'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return debt_as_percentage_of_gdp()


@cache('step')
def bubble_perception_factor():
    """
    Real Name: b'Bubble perception factor'
    Original Eqn: b'normalised currency value in dollars+normalised debt as percentage of GDP+normalised public approval rate\\\\ +normalised unemployment percentage-normalised wealth fund'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return normalised_currency_value_in_dollars() + normalised_debt_as_percentage_of_gdp(
    ) + normalised_public_approval_rate() + normalised_unemployment_percentage(
    ) - normalised_wealth_fund()


@cache('step')
def buying():
    """
    Real Name: b'Buying'
    Original Eqn: b'100/Market LCU pricing'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return 100 / market_lcu_pricing()


@cache('step')
def resulting_investments():
    """
    Real Name: b'Resulting investments'
    Original Eqn: b'Lithium demand/1000'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return lithium_demand() / 1000


@cache('run')
def initial_lcu_in_foreign_hands():
    """
    Real Name: b'Initial LCU in foreign hands'
    Original Eqn: b'500'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 500


@cache('step')
def selling():
    """
    Real Name: b'Selling'
    Original Eqn: b'100*Market LCU pricing*Normalised currency speculation sell'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return 100 * market_lcu_pricing() * normalised_currency_speculation_sell()


@cache('step')
def currency_speculation():
    """
    Real Name: b'Currency speculation'
    Original Eqn: b'INTEG ( Appreciation-Depreciation, Initial currency speculation)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_currency_speculation()


@cache('step')
def market_lcu_pricing():
    """
    Real Name: b'Market LCU pricing'
    Original Eqn: b'Tradeable LCU in foreign hands/LCU in the market'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return tradeable_lcu_in_foreign_hands() / lcu_in_the_market()


@cache('step')
def tradeable_lcu_in_foreign_hands():
    """
    Real Name: b'Tradeable LCU in foreign hands'
    Original Eqn: b'INTEG ( Buying+Decreasing investments-Increasing investments-Selling, Initial LCU in foreign hands)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_tradeable_lcu_in_foreign_hands()


@cache('step')
def total_imports_agr_ind_serv_in_lcu():
    """
    Real Name: b'Total imports AGR IND SERV in LCU'
    Original Eqn: b'"2010 imports in dollars"*Exchange rate'
    Units: b'LCU/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return _imports_in_dollars() * exchange_rate()


@cache('run')
def initial_currency_speculation():
    """
    Real Name: b'Initial currency speculation'
    Original Eqn: b'1e+06'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1e+06


@cache('step')
def normalised_currency_speculation_sell():
    """
    Real Name: b'Normalised currency speculation sell'
    Original Eqn: b'MAX(1,Currency speculation/1e+06)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(1, currency_speculation() / 1e+06)


@cache('step')
def reserved_for_investments():
    """
    Real Name: b'Reserved for investments'
    Original Eqn: b'INTEG ( Increasing investments-Decreasing investments, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_reserved_for_investments()


@cache('step')
def lcu_in_the_market():
    """
    Real Name: b'LCU in the market'
    Original Eqn: b'INTEG ( Selling-Buying, Initial LCU in market)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_lcu_in_the_market()


@cache('run')
def initial_lcu_in_market():
    """
    Real Name: b'Initial LCU in market'
    Original Eqn: b'500'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 500


@cache('step')
def national_unemployment_previous_year():
    """
    Real Name: b'national unemployment previous year'
    Original Eqn: b'DELAY FIXED(national unemployment percentage, 12, national unemployment percentage )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _delay_national_unemployment_percentage_round12__time_step___time_step_national_unemployment_percentage_12__time_step(
    )


@cache('step')
def debt():
    """
    Real Name: b'Debt'
    Original Eqn: b'INTEG ( Borrowing-Amortising, "2010 GDP"*"2014 debt as percentage of GDP")'
    Units: b'dollars'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_debt()


@cache('step')
def local_unemployment():
    """
    Real Name: b'local unemployment'
    Original Eqn: b'local population-labour demand'
    Units: b'persons'
    Limits: (None, None)
    Type: component

    b''
    """
    return local_population() - labour_demand()


@cache('step')
def public_approval_rate():
    """
    Real Name: b'public approval rate'
    Original Eqn: b'INTEG ( increasing popularity-decreasing popularity, 50)'
    Units: b'pct'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_public_approval_rate()


@cache('step')
def hdi_previous_year():
    """
    Real Name: b'HDI previous year'
    Original Eqn: b'DELAY FIXED(Human Development Index, 12, Human Development Index)'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return _delay_human_development_index_round12__time_step___time_step_human_development_index_12__time_step(
    )


@cache('step')
def decreasing_popularity():
    """
    Real Name: b'decreasing popularity'
    Original Eqn: b'IF THEN ELSE(Human Development Index < HDI previous year, 1, 0) + IF THEN ELSE(national unemployment percentage > national unemployment previous year,\\\\ 1, 0)'
    Units: b'pct/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        human_development_index() < hdi_previous_year(), 1, 0) + functions.if_then_else(
            national_unemployment_percentage() > national_unemployment_previous_year(), 1, 0)


@cache('step')
def national_unemployment_percentage():
    """
    Real Name: b'national unemployment percentage'
    Original Eqn: b'((Total population Chile * 0.07) + local unemployment )/Total population Chile'
    Units: b'pct'
    Limits: (None, None)
    Type: component

    b''
    """
    return ((total_population_chile() * 0.07) + local_unemployment()) / total_population_chile()


@cache('step')
def increasing_popularity():
    """
    Real Name: b'increasing popularity'
    Original Eqn: b'IF THEN ELSE(Human Development Index > HDI previous year, 1, 0) + IF THEN ELSE(national unemployment percentage < national unemployment previous year,\\\\ 1, 0)'
    Units: b'pct/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        human_development_index() > hdi_previous_year(), 1, 0) + functions.if_then_else(
            national_unemployment_percentage() < national_unemployment_previous_year(), 1, 0)


@cache('step')
def lithium_exports_in_lcu():
    """
    Real Name: b'Lithium exports in LCU'
    Original Eqn: b'Lithium exports in dollars/Currency value in dollars'
    Units: b'LCU/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return lithium_exports_in_dollars() / currency_value_in_dollars()


@cache('step')
def currency_value_in_dollars():
    """
    Real Name: b'Currency value in dollars'
    Original Eqn: b'0.75+(Lithium demand/250000)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return 0.75 + (lithium_demand() / 250000)


@cache('step')
def foreign_demand_agr_ind_serv_in_lcu():
    """
    Real Name: b'Foreign demand AGR IND SERV in LCU'
    Original Eqn: b'"2010 foreign demand AGR IND SERV in dollars"/Currency value in dollars'
    Units: b'LCU/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return _foreign_demand_agr_ind_serv_in_dollars() / currency_value_in_dollars()


@cache('step')
def gdp_in_real_terms():
    """
    Real Name: b'GDP in real terms'
    Original Eqn: b'GDP*Currency value in dollars'
    Units: b'dollar/person'
    Limits: (None, None)
    Type: component

    b''
    """
    return gdp() * currency_value_in_dollars()


@cache('step')
def foreign_investments_in_lcu():
    """
    Real Name: b'Foreign investments in LCU'
    Original Eqn: b'Foreign investments in dollars/Currency value in dollars'
    Units: b'LCU/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return foreign_investments_in_dollars() / currency_value_in_dollars()


@cache('step')
def total_exports_agr_ind_serv_in_lcu():
    """
    Real Name: b'Total exports AGR IND SERV in LCU'
    Original Eqn: b'IF THEN ELSE("Production capacity surplus/deficit">0, Foreign demand AGR IND SERV in LCU\\\\ , Domestic production capacity AGR IND SERV+Total imports AGR IND SERV in LCU-Domestic demand for AGR IND SERV\\\\ )'
    Units: b'LCU/year'
    Limits: (None, None)
    Type: component

    b"When there's enough production capacity in the country, the production \\n    \\t\\tsatisfies demand. In case of production 'shortage', domestic demand is \\n    \\t\\tprioritised and not all demand can be satisfied."
    """
    return functions.if_then_else(
        production_capacity_surplusdeficit() > 0, foreign_demand_agr_ind_serv_in_lcu(),
        domestic_production_capacity_agr_ind_serv() + total_imports_agr_ind_serv_in_lcu() -
        domestic_demand_for_agr_ind_serv())


@cache('step')
def gdp():
    """
    Real Name: b'GDP'
    Original Eqn: b'Domestic production capacity AGR IND SERV+Government expenditure+Foreign investments in LCU'
    Units: b'LCU/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return domestic_production_capacity_agr_ind_serv() + government_expenditure(
    ) + foreign_investments_in_lcu()


@cache('step')
def tax_income_in_dollars():
    """
    Real Name: b'Tax income in dollars'
    Original Eqn: b'GDP*Taxation rate*Currency value in dollars'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return gdp() * taxation_rate() * currency_value_in_dollars()


@cache('step')
def surplusdeficit():
    """
    Real Name: b'"Surplus/Deficit"'
    Original Eqn: b'Government income-Government expenditure*Currency value in dollars-Interest payments'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return government_income(
    ) - government_expenditure() * currency_value_in_dollars() - interest_payments()


@cache('run')
def _foreign_demand_agr_ind_serv_in_dollars():
    """
    Real Name: b'"2010 foreign demand AGR IND SERV in dollars"'
    Original Eqn: b'0.377451*2.185e+11'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.377451 * 2.185e+11


@cache('run')
def _foreign_investment():
    """
    Real Name: b'"2010 foreign investment"'
    Original Eqn: b'1.60161e+10'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1.60161e+10


@cache('run')
def _imports_in_dollars():
    """
    Real Name: b'"2010 imports in dollars"'
    Original Eqn: b'6.8e+10'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 6.8e+10


@cache('step')
def interest_payments():
    """
    Real Name: b'Interest payments'
    Original Eqn: b'Interest rate*Debt'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return interest_rate() * debt()


@cache('run')
def interest_rate():
    """
    Real Name: b'Interest rate'
    Original Eqn: b'0.02'
    Units: b'1/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.02


@cache('step')
def foreign_investments_in_dollars():
    """
    Real Name: b'Foreign investments in dollars'
    Original Eqn: b'"2010 foreign investment"*(Lithium demand/40886)'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return _foreign_investment() * (lithium_demand() / 40886)


@cache('run')
def _debt_as_percentage_of_gdp():
    """
    Real Name: b'"2014 debt as percentage of GDP"'
    Original Eqn: b'0.151'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.151


@cache('step')
def domestic_demand_for_agr_ind_serv():
    """
    Real Name: b'Domestic demand for AGR IND SERV'
    Original Eqn: b'GDP*"Fraction GDP/consumer consumption"'
    Units: b'LCU/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return gdp() * fraction_gdpconsumer_consumption()


@cache('step')
def gdp_per_capita_in_lcu():
    """
    Real Name: b'GDP per capita in LCU'
    Original Eqn: b'GDP/Total population Chile'
    Units: b'LCU/person'
    Limits: (None, None)
    Type: component

    b''
    """
    return gdp() / total_population_chile()


@cache('step')
def lithium_exports_in_dollars():
    """
    Real Name: b'Lithium exports in dollars'
    Original Eqn: b'production * global market price per metric ton'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return production() * global_market_price_per_metric_ton()


@cache('step')
def government_expenditure():
    """
    Real Name: b'Government expenditure'
    Original Eqn: b'Social spending+New HD spending+Investment in wealth fund'
    Units: b'LCU/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return social_spending() + new_hd_spending() + investment_in_wealth_fund()


@cache('step')
def government_income():
    """
    Real Name: b'Government income'
    Original Eqn: b'government income from lithium mining+Tax income in dollars'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return government_income_from_lithium_mining() + tax_income_in_dollars()


@cache('step')
def debt_as_percentage_of_gdp():
    """
    Real Name: b'Debt as percentage of GDP'
    Original Eqn: b'Debt/GDP in real terms'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return debt() / gdp_in_real_terms()


@cache('step')
def decommissioning():
    """
    Real Name: b'decommissioning'
    Original Eqn: b'IF THEN ELSE("Production capacity surplus/deficit" > 0 , DELAY3( "Production capacity surplus/deficit", Decommissioning delay ) , 0 )'
    Units: b'LCU/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        production_capacity_surplusdeficit() > 0,
        _delay_production_capacity_surplusdeficit_decommissioning_delay_production_capacity_surplusdeficit_3(
        ), 0)


@cache('run')
def decommissioning_delay():
    """
    Real Name: b'Decommissioning delay'
    Original Eqn: b'12'
    Units: b'Months'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 12


@cache('step')
def new_production_capacity():
    """
    Real Name: b'new production capacity'
    Original Eqn: b'IF THEN ELSE("Production capacity surplus/deficit"<0,DELAY3( -"Production capacity surplus/deficit"\\\\ , New production capacity delay ) ,0 )'
    Units: b'LCU/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        production_capacity_surplusdeficit() < 0,
        _delay_production_capacity_surplusdeficit_new_production_capacity_delay_production_capacity_surplusdeficit_3(
        ), 0)


@cache('step')
def domestic_production_capacity_agr_ind_serv():
    """
    Real Name: b'Domestic production capacity AGR IND SERV'
    Original Eqn: b'INTEG ( new production capacity-decommissioning, Init domestic production capacity)'
    Units: b'LCU/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_domestic_production_capacity_agr_ind_serv()


@cache('step')
def income_index():
    """
    Real Name: b'income index'
    Original Eqn: b'(LN(Gross National Income per capita) - LN(100)) / (LN(75000) - LN(100))'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (np.log(gross_national_income_per_capita()) - np.log(100)) / (np.log(75000) -
                                                                         np.log(100))


@cache('run')
def init_domestic_production_capacity():
    """
    Real Name: b'Init domestic production capacity'
    Original Eqn: b'1.54e+11'
    Units: b'LCU/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1.54e+11


@cache('run')
def new_production_capacity_delay():
    """
    Real Name: b'New production capacity delay'
    Original Eqn: b'96'
    Units: b'Months'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 96


@cache('step')
def total_exports():
    """
    Real Name: b'Total exports'
    Original Eqn: b'Lithium exports in LCU+Total exports AGR IND SERV in LCU'
    Units: b'LCU/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return lithium_exports_in_lcu() + total_exports_agr_ind_serv_in_lcu()


@cache('step')
def production_capacity_surplusdeficit():
    """
    Real Name: b'"Production capacity surplus/deficit"'
    Original Eqn: b'+Domestic production capacity AGR IND SERV +Total imports AGR IND SERV in LCU -Foreign demand AGR IND SERV in LCU -Domestic demand for AGR IND SERV'
    Units: b'LCU/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return domestic_production_capacity_agr_ind_serv() + total_imports_agr_ind_serv_in_lcu(
    ) - foreign_demand_agr_ind_serv_in_lcu() - domestic_demand_for_agr_ind_serv()


@cache('run')
def fraction_gdpconsumer_consumption():
    """
    Real Name: b'"Fraction GDP/consumer consumption"'
    Original Eqn: b'1.54e+11/2.38e+11'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1.54e+11 / 2.38e+11


@cache('step')
def gross_national_income_per_capita():
    """
    Real Name: b'Gross National Income per capita'
    Original Eqn: b'GDP in real terms/Total population Chile'
    Units: b'dollar/year/person'
    Limits: (None, None)
    Type: component

    b''
    """
    return gdp_in_real_terms() / total_population_chile()


@cache('run')
def taxation_rate():
    """
    Real Name: b'Taxation rate'
    Original Eqn: b'0.2'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.2


@cache('run')
def _life_expectancy():
    """
    Real Name: b'"2010 Life expectancy"'
    Original Eqn: b'78.454'
    Units: b'years'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 78.454


@cache('run')
def _lithium_production():
    """
    Real Name: b'"2010 Lithium production"'
    Original Eqn: b'40886'
    Units: b'metric ton/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 40886


@cache('run')
def _mys():
    """
    Real Name: b'"2010 MYS"'
    Original Eqn: b'9.8'
    Units: b'years'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 9.8


@cache('run')
def investment_in_wealth_fund():
    """
    Real Name: b'Investment in wealth fund'
    Original Eqn: b'0'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def amortising():
    """
    Real Name: b'Amortising'
    Original Eqn: b'IF THEN ELSE("Surplus/Deficit"<0, -"Surplus/Deficit"/12 , 0 )'
    Units: b'dollars/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(surplusdeficit() < 0, -surplusdeficit() / 12, 0)


@cache('step')
def wealth_fund():
    """
    Real Name: b'Wealth fund'
    Original Eqn: b'INTEG ( Saving, 0)'
    Units: b'dollars'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_wealth_fund()


@cache('step')
def borrowing():
    """
    Real Name: b'Borrowing'
    Original Eqn: b'IF THEN ELSE("Surplus/Deficit">0, "Surplus/Deficit"/12 , 0 )'
    Units: b'dollars/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(surplusdeficit() > 0, surplusdeficit() / 12, 0)


@cache('step')
def life_expectancy():
    """
    Real Name: b'Life expectancy'
    Original Eqn: b'DELAY3I(Health expenditure/(Total population Chile*Money per year of extra living)+"2010 Life expectancy"\\\\ ,Health system delay , "2010 Life expectancy" )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _delay_health_expendituretotal_population_chilemoney_per_year_of_extra_living_life_expectancy_health_system_delay__life_expectancy_3(
    )


@cache('step')
def life_expectancy_index():
    """
    Real Name: b'Life Expectancy Index'
    Original Eqn: b'(Life expectancy - 20) / ( 85 - 20 )'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (life_expectancy() - 20) / (85 - 20)


@cache('step')
def mean_years_of_schooling_index():
    """
    Real Name: b'mean years of schooling index'
    Original Eqn: b'Mean years of schooling/15'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return mean_years_of_schooling() / 15


@cache('step')
def mean_years_of_schooling():
    """
    Real Name: b'Mean years of schooling'
    Original Eqn: b'DELAY3I( (Education expenditure)/(Total population Chile*Money per year of extra education\\\\ ) , Edu system delay, "2010 MYS" )'
    Units: b'years'
    Limits: (None, None)
    Type: component

    b''
    """
    return _delay_education_expendituretotal_population_chilemoney_per_year_of_extra_education_edu_system_delay__mys_3(
    )


@cache('run')
def education_fraction():
    """
    Real Name: b'Education Fraction'
    Original Eqn: b'0.37'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.37


@cache('run')
def health_fraction():
    """
    Real Name: b'Health Fraction'
    Original Eqn: b'0.63'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.63


@cache('step')
def saving():
    """
    Real Name: b'Saving'
    Original Eqn: b'Investment in wealth fund/12'
    Units: b'dollars/Month'
    Limits: (None, None)
    Type: component

    b''
    """
    return investment_in_wealth_fund() / 12


@cache('step')
def human_development_spending():
    """
    Real Name: b'Human Development spending'
    Original Eqn: b'New HD spending'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return new_hd_spending()


@cache('step')
def education_expenditure():
    """
    Real Name: b'Education expenditure'
    Original Eqn: b'Education Fraction*Human Development spending'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return education_fraction() * human_development_spending()


@cache('run')
def new_hd_spending():
    """
    Real Name: b'New HD spending'
    Original Eqn: b'1'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def productivity_mining_sector():
    """
    Real Name: b'Productivity mining sector'
    Original Eqn: b'"2010 Lithium production"/People working in mining sector in 2017'
    Units: b'metric ton/(year*person)'
    Limits: (None, None)
    Type: component

    b''
    """
    return _lithium_production() / people_working_in_mining_sector_in_2017()


@cache('run')
def social_spending():
    """
    Real Name: b'Social spending'
    Original Eqn: b'2.185e+11-1.68e+11'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 2.185e+11 - 1.68e+11


@cache('step')
def health_expenditure():
    """
    Real Name: b'Health expenditure'
    Original Eqn: b'Health Fraction*Human Development spending'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return health_fraction() * human_development_spending()


@cache('step')
def agriculture_water_use():
    """
    Real Name: b'agriculture water use'
    Original Eqn: b'water efficiency of agriculture*government agriculture research investment factor*0'
    Units: b'm3/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return water_efficiency_of_agriculture() * government_agriculture_research_investment_factor(
    ) * 0


@cache('run')
def natural_replenishing():
    """
    Real Name: b'natural replenishing'
    Original Eqn: b'0.016*3e+09/0.1'
    Units: b'm3/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.016 * 3e+09 / 0.1


@cache('run')
def government_agriculture_research_investment_factor():
    """
    Real Name: b'government agriculture research investment factor'
    Original Eqn: b'1'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def labour_demand():
    """
    Real Name: b'labour demand'
    Original Eqn: b'production/Productivity mining sector'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return production() / productivity_mining_sector()


@cache('run')
def labour_participation_rate_in_2019():
    """
    Real Name: b'Labour participation rate in 2019'
    Original Eqn: b'0.595'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.595


@cache('run')
def people_working_in_mining_sector_in_2017():
    """
    Real Name: b'People working in mining sector in 2017'
    Original Eqn: b'1.805e+07*0.029'
    Units: b'persons'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1.805e+07 * 0.029


@cache('run')
def migration_out():
    """
    Real Name: b'migration out'
    Original Eqn: b'0'
    Units: b'persons/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def per_capita_water_use():
    """
    Real Name: b'Per capita water use'
    Original Eqn: b'0.1*365'
    Units: b'm3/person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1 * 365


@cache('step')
def replenishing():
    """
    Real Name: b'Replenishing'
    Original Eqn: b'IF THEN ELSE(water use<natural replenishing, 1 ,0)'
    Units: b'Dmnl/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(water_use() < natural_replenishing(), 1, 0)


@cache('step')
def water_use():
    """
    Real Name: b'water use'
    Original Eqn: b'mining water use+industry water use+domestic water use+agriculture water use'
    Units: b'm3/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return mining_water_use() + industry_water_use() + domestic_water_use(
    ) + agriculture_water_use()


@cache('run')
def water_required_per_metric_ton_of_lithium_mined():
    """
    Real Name: b'water required per metric ton of lithium mined'
    Original Eqn: b'500000'
    Units: b'm3/metric ton'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 500000


@cache('run')
def industry_water_use():
    """
    Real Name: b'industry water use'
    Original Eqn: b'0'
    Units: b'm3/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def migration_in():
    """
    Real Name: b'migration in'
    Original Eqn: b'DELAY1I( IF THEN ELSE(labour demand > local population*Labour participation rate in 2019\\\\ , labour demand/Labour participation rate in 2019 - local population, 0), 3, (labour demand\\\\ /Labour participation rate in 2019-local population )/12)'
    Units: b''
    Limits: (None, None)
    Type: component

    b'migration time is 3 months, but check!'
    """
    return _delay_functionsif_then_elselabour_demandlocal_populationlabour_participation_rate_in_2019labour_demandlabour_participation_rate_in_2019local_population0_3_labour_demandlabour_participation_rate_in_2019local_population12_1(
    )


@cache('run')
def water_efficiency_of_agriculture():
    """
    Real Name: b'water efficiency of agriculture'
    Original Eqn: b'1'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def overuse():
    """
    Real Name: b'"Over-use"'
    Original Eqn: b'IF THEN ELSE(water use>natural replenishing, 1 , 0)'
    Units: b'Dmnl/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(water_use() > natural_replenishing(), 1, 0)


@cache('step')
def water_stress():
    """
    Real Name: b'Water stress'
    Original Eqn: b'INTEG ( "Over-use"-Replenishing, 0)'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_water_stress()


@cache('step')
def water_stocks():
    """
    Real Name: b'water stocks'
    Original Eqn: b'INTEG ( natural replenishing-water use, 2.3e+10)'
    Units: b'm3'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_water_stocks()


@cache('run')
def change_in_eys():
    """
    Real Name: b'change in EYS'
    Original Eqn: b'0'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def chilean_lithium_in_use_globally():
    """
    Real Name: b'chilean lithium in use globally'
    Original Eqn: b'INTEG ( production, 0)'
    Units: b'metric ton'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_chilean_lithium_in_use_globally()


@cache('step')
def corporate_income_from_lithium_mining():
    """
    Real Name: b'corporate income from lithium mining'
    Original Eqn: b'IF THEN ELSE( nationalisation SWITCH=0 , global market price per metric ton*production\\\\ , 0 )'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(nationalisation_switch() == 0,
                                  global_market_price_per_metric_ton() * production(), 0)


@cache('step')
def lce_demand():
    """
    Real Name: b'LCE demand'
    Original Eqn: b'Lithium demand'
    Units: b'metric ton/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return lithium_demand()


@cache('step')
def domestic_water_use():
    """
    Real Name: b'domestic water use'
    Original Eqn: b'Per capita water use*local population'
    Units: b'm3/year'
    Limits: (None, None)
    Type: component

    b'1.5 mil people dependent on local water sources'
    """
    return per_capita_water_use() * local_population()


@cache('run')
def edu_system_delay():
    """
    Real Name: b'Edu system delay'
    Original Eqn: b'3*12'
    Units: b'Months'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 3 * 12


@cache('step')
def education_index():
    """
    Real Name: b'Education index'
    Original Eqn: b'(mean years of schooling index + expected years of schooling index) / 2'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (mean_years_of_schooling_index() + expected_years_of_schooling_index()) / 2


@cache('step')
def efficiency_factor():
    """
    Real Name: b'efficiency factor'
    Original Eqn: b'mining expertise'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return mining_expertise()


@cache('step')
def expected_years_of_schooling():
    """
    Real Name: b'Expected Years of Schooling'
    Original Eqn: b'INTEG ( change in EYS, initial EYS)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_expected_years_of_schooling()


@cache('step')
def expected_years_of_schooling_index():
    """
    Real Name: b'expected years of schooling index'
    Original Eqn: b'Expected Years of Schooling/18'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return expected_years_of_schooling() / 18


@cache('step')
def fraction_of_population_dependent_on_mining_sector():
    """
    Real Name: b'fraction of population dependent on mining sector'
    Original Eqn: b'labour demand/Total population Chile'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return labour_demand() / total_population_chile()


@cache('step')
def fraction_of_population_dependent_on_other_sectors():
    """
    Real Name: b'fraction of population dependent on other sectors'
    Original Eqn: b'Total population Chile'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return total_population_chile()


@cache('run')
def global_market_price_per_metric_ton():
    """
    Real Name: b'global market price per metric ton'
    Original Eqn: b'17000'
    Units: b'dollars/metric ton'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 17000


@cache('step')
def government_income_from_lithium_mining():
    """
    Real Name: b'government income from lithium mining'
    Original Eqn: b'IF THEN ELSE(nationalisation SWITCH=1, global market price per metric ton*production\\\\ , corporate income from lithium mining*Taxation )'
    Units: b'dollars/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(nationalisation_switch() == 1,
                                  global_market_price_per_metric_ton() * production(),
                                  corporate_income_from_lithium_mining() * taxation())


@cache('run')
def government_mining_research_investment_factor():
    """
    Real Name: b'government mining research investment factor'
    Original Eqn: b'1'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('run')
def health_system_delay():
    """
    Real Name: b'Health system delay'
    Original Eqn: b'3'
    Units: b'years'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 3


@cache('step')
def human_development_index():
    """
    Real Name: b'Human Development Index'
    Original Eqn: b'(Life Expectancy Index * Education index * income index) ^ (1/3)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (life_expectancy_index() * education_index() * income_index())**(1 / 3)


@cache('run')
def initial_eys():
    """
    Real Name: b'initial EYS'
    Original Eqn: b'16.4'
    Units: b'years'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 16.4


@cache('run')
def initial_identified_reserves():
    """
    Real Name: b'initial identified reserves'
    Original Eqn: b'7.5e+06'
    Units: b'metric ton'
    Limits: (None, None)
    Type: constant

    b'depends on year of initiation, in LiCO3 equivalent'
    """
    return 7.5e+06


@cache('run')
def initial_local_population():
    """
    Real Name: b'initial local population'
    Original Eqn: b'1.5e+06'
    Units: b'persons'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1.5e+06


@cache('run')
def initial_population():
    """
    Real Name: b'initial population'
    Original Eqn: b'1.82e+07'
    Units: b'persons'
    Limits: (None, None)
    Type: constant

    b'depends on year of initiation'
    """
    return 1.82e+07


@cache('step')
def lithium_salt_reserves():
    """
    Real Name: b'lithium salt reserves'
    Original Eqn: b'INTEG ( -loss-production, initial identified reserves)'
    Units: b'metric ton'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_lithium_salt_reserves()


@cache('step')
def local_population():
    """
    Real Name: b'local population'
    Original Eqn: b'INTEG ( migration in-migration out, initial local population)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_local_population()


@cache('step')
def loss():
    """
    Real Name: b'loss'
    Original Eqn: b'(1-efficiency factor)*LCE demand'
    Units: b'metric ton/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return (1 - efficiency_factor()) * lce_demand()


@cache('step')
def mining_expertise():
    """
    Real Name: b'mining expertise'
    Original Eqn: b'IF THEN ELSE(nationalisation SWITCH=1,0.6*government mining research investment factor\\\\ , 0.8 )'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b'factor between 0 and 1'
    """
    return functions.if_then_else(nationalisation_switch() == 1,
                                  0.6 * government_mining_research_investment_factor(), 0.8)


@cache('step')
def mining_water_use():
    """
    Real Name: b'mining water use'
    Original Eqn: b'production * water required per metric ton of lithium mined * (1- mining expertise)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return production() * water_required_per_metric_ton_of_lithium_mined() * (1 -
                                                                              mining_expertise())


@cache('run')
def money_per_year_of_extra_education():
    """
    Real Name: b'Money per year of extra education'
    Original Eqn: b'500/1.4'
    Units: b'dollars/(year*year*person)'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 500 / 1.4


@cache('run')
def money_per_year_of_extra_living():
    """
    Real Name: b'Money per year of extra living'
    Original Eqn: b'800/2.5'
    Units: b'dollars/(year*year*person)'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 800 / 2.5


@cache('run')
def nationalisation_switch():
    """
    Real Name: b'nationalisation SWITCH'
    Original Eqn: b'0'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def net_population_growth():
    """
    Real Name: b'net population growth'
    Original Eqn: b'185700/12'
    Units: b'persons/Month'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 185700 / 12


@cache('step')
def production():
    """
    Real Name: b'production'
    Original Eqn: b'LCE demand'
    Units: b'metric ton/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return lce_demand()


@cache('run')
def taxation():
    """
    Real Name: b'Taxation'
    Original Eqn: b'0.7'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.7


@cache('step')
def total_population_chile():
    """
    Real Name: b'Total population Chile'
    Original Eqn: b'INTEG ( net population growth, initial population)'
    Units: b'persons'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_total_population_chile()


@cache('run')
def final_time():
    """
    Real Name: b'FINAL TIME'
    Original Eqn: b'5'
    Units: b'Month'
    Limits: (None, None)
    Type: constant

    b'The final time for the simulation.'
    """
    return 5


@cache('run')
def initial_time():
    """
    Real Name: b'INITIAL TIME'
    Original Eqn: b'0'
    Units: b'Month'
    Limits: (None, None)
    Type: constant

    b'The initial time for the simulation.'
    """
    return 0


@cache('step')
def saveper():
    """
    Real Name: b'SAVEPER'
    Original Eqn: b'TIME STEP'
    Units: b'Month'
    Limits: (0.0, None)
    Type: component

    b'The frequency with which output is stored.'
    """
    return time_step()


@cache('run')
def time_step():
    """
    Real Name: b'TIME STEP'
    Original Eqn: b'0.015625'
    Units: b'Month'
    Limits: (0.0, None)
    Type: constant

    b'The time step for the simulation.'
    """
    return 0.015625


_integ_currency_speculation = functions.Integ(lambda: appreciation() - depreciation(), lambda:
                                              initial_currency_speculation())

_integ_tradeable_lcu_in_foreign_hands = functions.Integ(
    lambda: buying() + decreasing_investments() - increasing_investments() - selling(), lambda:
    initial_lcu_in_foreign_hands())

_integ_reserved_for_investments = functions.Integ(
    lambda: increasing_investments() - decreasing_investments(), lambda: 0)

_integ_lcu_in_the_market = functions.Integ(lambda: selling() - buying(), lambda:
                                           initial_lcu_in_market())

_delay_national_unemployment_percentage_round12__time_step___time_step_national_unemployment_percentage_12__time_step = functions.Delay(
    lambda: national_unemployment_percentage(), lambda: round(12 / time_step()) * time_step(),
    lambda: national_unemployment_percentage(), lambda: 12 / time_step())

_integ_debt = functions.Integ(lambda: borrowing() - amortising(), lambda: _gdp() *
                              _debt_as_percentage_of_gdp())

_integ_public_approval_rate = functions.Integ(
    lambda: increasing_popularity() - decreasing_popularity(), lambda: 50)

_delay_human_development_index_round12__time_step___time_step_human_development_index_12__time_step = functions.Delay(
    lambda: human_development_index(), lambda: round(12 / time_step()) * time_step(), lambda:
    human_development_index(), lambda: 12 / time_step())

_delay_production_capacity_surplusdeficit_decommissioning_delay_production_capacity_surplusdeficit_3 = functions.Delay(
    lambda: production_capacity_surplusdeficit(), lambda: decommissioning_delay(), lambda:
    production_capacity_surplusdeficit(), lambda: 3)

_delay_production_capacity_surplusdeficit_new_production_capacity_delay_production_capacity_surplusdeficit_3 = functions.Delay(
    lambda: -production_capacity_surplusdeficit(), lambda: new_production_capacity_delay(), lambda:
    -production_capacity_surplusdeficit(), lambda: 3)

_integ_domestic_production_capacity_agr_ind_serv = functions.Integ(
    lambda: new_production_capacity() - decommissioning(), lambda:
    init_domestic_production_capacity())

_integ_wealth_fund = functions.Integ(lambda: saving(), lambda: 0)

_delay_health_expendituretotal_population_chilemoney_per_year_of_extra_living_life_expectancy_health_system_delay__life_expectancy_3 = functions.Delay(
    lambda: health_expenditure() / (total_population_chile() * money_per_year_of_extra_living()) +
    _life_expectancy(), lambda: health_system_delay(), lambda: _life_expectancy(), lambda: 3)

_delay_education_expendituretotal_population_chilemoney_per_year_of_extra_education_edu_system_delay__mys_3 = functions.Delay(
    lambda: (education_expenditure()) / (
        total_population_chile() * money_per_year_of_extra_education()), lambda: edu_system_delay(
        ), lambda: _mys(), lambda: 3)

_delay_functionsif_then_elselabour_demandlocal_populationlabour_participation_rate_in_2019labour_demandlabour_participation_rate_in_2019local_population0_3_labour_demandlabour_participation_rate_in_2019local_population12_1 = functions.Delay(
    lambda: functions.if_then_else(
        labour_demand() > local_population() * labour_participation_rate_in_2019(),
        labour_demand() / labour_participation_rate_in_2019() - local_population(), 0), lambda: 3,
    lambda: (labour_demand() / labour_participation_rate_in_2019() - local_population()
             ) / 12, lambda: 1)

_integ_water_stress = functions.Integ(lambda: overuse() - replenishing(), lambda: 0)

_integ_water_stocks = functions.Integ(lambda: natural_replenishing() - water_use(), lambda: 2.3e+10
                                      )

_integ_chilean_lithium_in_use_globally = functions.Integ(lambda: production(), lambda: 0)

_integ_expected_years_of_schooling = functions.Integ(lambda: change_in_eys(), lambda: initial_eys(
))

_integ_lithium_salt_reserves = functions.Integ(lambda: -loss() - production(), lambda:
                                               initial_identified_reserves())

_integ_local_population = functions.Integ(lambda: migration_in() - migration_out(), lambda:
                                          initial_local_population())

_integ_total_population_chile = functions.Integ(lambda: net_population_growth(), lambda:
                                                initial_population())
