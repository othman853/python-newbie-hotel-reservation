# This is a god file, no OO, no organization, no tests, just code.
import re as regex

# Hardcoding data
lakewood_weekend_regular_price = {'customer_type': 'regular', 'weekend': True, 'value': 90}
lakewood_weekday_regular_price = {'customer_type': 'regular', 'weekend': False, 'value': 110}
lakewood_weekend_rewards_price = {'customer_type': 'rewards', 'weekend': True, 'value': 80}
lakewood_weekday_rewards_price = {'customer_type': 'rewards', 'weekend': False, 'value': 80}

bridgewood_weekend_regular_price = {'customer_type': 'regular', 'weekend': True, 'value': 60}
bridgewood_weekday_regular_price = {'customer_type': 'regular', 'weekend': False, 'value': 160}
bridgewood_weekend_rewards_price = {'customer_type': 'rewards', 'weekend': True, 'value': 50}
bridgewood_weekday_rewards_price = {'customer_type': 'rewards', 'weekend': False, 'value': 110}

ridgewood_weekend_regular_price = {'customer_type': 'regular', 'weekend': True, 'value': 150}
ridgewood_weekday_regular_price = {'customer_type': 'regular', 'weekend': False, 'value': 220}
ridgewood_weekend_rewards_price = {'customer_type': 'rewards', 'weekend': True, 'value': 40}
ridgewood_weekday_rewards_price = {'customer_type': 'rewards', 'weekend': False, 'value': 100}


lakewood_prices = [lakewood_weekend_regular_price, lakewood_weekday_regular_price, lakewood_weekend_rewards_price, lakewood_weekday_rewards_price]
bridgewood_prices = [bridgewood_weekend_regular_price, bridgewood_weekday_regular_price, bridgewood_weekend_rewards_price, bridgewood_weekday_rewards_price]
ridgewood_prices = [ridgewood_weekend_regular_price, ridgewood_weekday_regular_price, ridgewood_weekend_rewards_price, ridgewood_weekday_rewards_price]

lakewood = {"name": "Lakewood", "rating": 3, "prices": lakewood_prices}
bridgewood = {"name": "Bridgewood", "rating": 4 , "prices": bridgewood_prices}
ridgewood = {"name": "Ridgewood", "rating": 5, "prices": ridgewood_prices}

hotels = [lakewood, bridgewood, ridgewood]

# ridgewood = {name: 'Ridgewood', prices: [{}, {}, {}, {}]}

# hotels = [bridgewood, ridgewood]

# Compiling a Regex using the raw string python notation (with the preceding r)
# By now, the regex accepts anything
customer_type_pattern = regex.compile(r're(gular|wards)')

#Sample: 16Mar2009(mon), 17Apr2010(mon) ...
reservation_date_pattern = regex.compile(r'\d{2}\w{3}\d{4}')

def print_file(file):
    line_number = 1
    for line in file:

        # Using match() instead of search() to get the pattern at index 0
        if customer_type_pattern.match(line.lower()) and reservation_date_pattern.findall(line):

            customer_type = customer_type_pattern.match(line.lower()).group(0)

            # Using findall to match same pattern multiple times
            # on a same string
            dates = reservation_date_pattern.findall(line)
            print customer_type
            print dates

        else:
            print 'Entry at line %d is invalid' % line_number
        line_number = line_number + 1

def classify(customer_type, dates):
    pass


entry_file = open('entries_sample')
print_file(entry_file)
