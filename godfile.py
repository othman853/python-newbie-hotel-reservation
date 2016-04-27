# This is a god file, no OO, no organization, no tests, just code.
import re as regex
from datetime import date as native_date

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

customer_type_pattern = regex.compile(r're(gular|wards)')

reservation_date_pattern = regex.compile(r'\d{2}\w{3}\d{4}')

def print_file(file):
    line_number = 1
    for line in file:

        if customer_type_pattern.match(line.lower()) and reservation_date_pattern.findall(line):

            customer_type = customer_type_pattern.match(line.lower()).group(0)
            dates = reservation_date_pattern.findall(line)

            cheapest_hotel = classify(customer_type, dates)

            print cheapest_hotel

        else:
            print 'Entry at line %d is invalid' % line_number
        line_number = line_number + 1

def classify(customer_type, dates):
    cheapest_hotel_name = None
    cheapest_hotel_price = None

    for hotel in hotels:
        current_hotel_name, current_hotel_price = calculate_hotel_price_for_reservation(hotel, customer_type, dates)

        if cheapest_hotel_price == None or cheapest_hotel_price > current_hotel_price:
            cheapest_hotel_name = current_hotel_name
            cheapest_hotel_price = current_hotel_price

    return cheapest_hotel_name


def calculate_hotel_price_for_reservation(hotel, customer_type, dates):
    hotel_prices = hotel['prices']
    prices_for_customer_type = [price for price in hotel_prices if price['customer_type'] == customer_type]

    date_prices = []
    for date in dates:
        price = filter(lambda p: p['weekend'] == is_weekend(date), prices_for_customer_type)
        date_prices.append(price[0]['value'])

    return hotel['name'], sum(date_prices)


def is_weekend(date):

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    day = int(date[0:2])
    month = date[2:5]
    month_number = months.index(month)
    year = int(date[5:9])

    to_date = native_date(year, month_number, day)

    return to_date.weekday() > 4


entry_file = open('entries_sample')
print_file(entry_file)
