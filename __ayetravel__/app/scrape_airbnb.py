from bs4 import BeautifulSoup
import requests


# User defined variables
user_specified_city = 'Chicago'
user_specified_state = 'IL'
user_specified_country = 'United-States'
user_specified_country_split = user_specified_country.split('-')
user_specified_country_split = user_specified_country_split[0] + ' ' + user_specified_country_split[1]
number_of_adults = 1

# URL variables
base_url = f'https://www.airbnb.com/s/{user_specified_city}--{user_specified_state}--{user_specified_country}' \
      f'/homes?refinement_paths[]=%2Fhomes&query=' \
      f'{user_specified_city}%2C {user_specified_state}%2C {user_specified_country_split}' \
      f'&allow_override[]=&adults={number_of_adults}'
cleaned_url = requests.get(base_url)
airbnb_soup = BeautifulSoup(cleaned_url.text, 'lxml')
airbnb_listing_div = airbnb_soup.find_all('div', attrs={'class': '_1df8dftk'}, limit=100)


def main():
    # for listing in airbnb_listings:
    #     print(listing.prettify())
    print(airbnb_listing_div)


if __name__ == '__main__':
    main()


# TODO test code for airbnb scraper
# import time
# from urllib.request import urlopen
#
# from bs4 import BeautifulSoup
# import re
# import requests
#
# hdr = {'User-Agent':
#        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
#
# list_urls = []
# prepostfixlist = [['https://www.airbnb.com/s/New-York--NY?ss_id=q1z6m0pk&page=','&s_tag=Swm8IKOK'],
#                   ['https://www.airbnb.com/s/San-Francisco--CA?ss_id=ng0pw1xp&page=','&s_tag=He2d5ecU'],
#                   ['https://www.airbnb.com/s/Los-Angeles?ss_id=gxqwgcby&page=','&s_tag=nhhRjOBR']]
# for prepostfix in prepostfixlist:
#     for i in range(1,18):
#         current_url = prepostfix[0] + str(i) + prepostfix[1]
#         # start_urls.append(current_url)
#         req = requests.get(current_url, headers=hdr)
#         # r = urllib2.urlopen(req).read()
#         with urlopen(req).read() as conn:
#             soup = BeautifulSoup(conn, "lxml")
#             for link in soup('a'):
#                 try:
#                     link['class']
#                 except KeyError:
#                     continue
#                 if link['class'] == ['media-photo','media-cover']:
#                     list_urls.append(link['href'])
#
#
# items = []
# prefix = 'https://www.airbnb.com'
# counter = 0
# for list_url in list_urls:
#     counter += 1
#     print("Number of pages scraped = " + str(counter))
#     # Make a 10-second delay to avoid exceeding rate limit.
#     time.sleep(10)
#     req = requests.get(prefix + list_url, headers=hdr)
#     # r = urllib2.urlopen(req).read()
#     with urlopen(req).read() as conn:
#         soup = BeautifulSoup(conn, "lxml")
#         item = {}
#         for metadat in soup('meta'):
#             try:
#                 metadat['content']
#             except KeyError:
#                 continue
#             if 'nightly_price' in metadat['content']:
#                 line = re.sub('false','False',metadat['content'])
#                 line = re.sub('true','True',line)
#                 line = re.sub('null','None',line)
#                 # Potential security flaw here! Might want to find a way to avoid eval.
#                 line = eval(line)
#                 nightly_price = int(line['nightly_price'].strip('$'))
#                 item['price'] = nightly_price
#                 item['isMonthly'] = line['isMonthly']
#                 item['minNights'] = line['minNights']
#                 for x in ['hosting_id','bed_type','cancel_policy','checkin_rating','cleanliness_rating','communication_rating','guest_satisfaction_overall','is_superhost','location_rating','person_capacity','picture_count','room_type','saved_to_wishlist_count','value_rating','visible_review_count']:
#                     item[x] = line['airEventData'][x]
#                 if 1 in line['airEventData']['amenities']:
#                     item['hasKitchen'] = True
#                 else:
#                     item['hasKitchen'] = False
#                 if 2 in line['airEventData']['amenities'] or 11 in line['airEventData']['amenities']:
#                     item['hasInternet'] = True
#                 else:
#                     item['hasInternet'] = False
#                 if 3 in line['airEventData']['amenities']:
#                     item['hasTV'] = True
#                 else:
#                     item['hasTV'] = False
#                 if 4 in line['airEventData']['amenities']:
#                     item['hasEssentials'] = True
#                 else:
#                     item['hasEssentials'] = False
#                 if 5 in line['airEventData']['amenities']:
#                     item['hasShampoo'] = True
#                 else:
#                     item['hasShampoo'] = False
#                 if 6 in line['airEventData']['amenities']:
#                     item['hasHeating'] = True
#                 else:
#                     item['hasHeating'] = False
#                 if 7 in line['airEventData']['amenities']:
#                     item['hasAC'] = True
#                 else:
#                     item['hasAC'] = False
#                 if 8 in line['airEventData']['amenities']:
#                     item['hasWasher'] = True
#                 else:
#                     item['hasWasher'] = False
#                 if 9 in line['airEventData']['amenities']:
#                     item['hasDryer'] = True
#                 else:
#                     item['hasDryer'] = False
#                 if 10 in line['airEventData']['amenities']:
#                     item['hasFreeParking'] = True
#                 else:
#                     item['hasFreeParking'] = False
#                 if 12 in line['airEventData']['amenities']:
#                     item['hasCable'] = True
#                 else:
#                     item['hasCable'] = False
#                 if 13 in line['airEventData']['amenities']:
#                     item['hasBreakfast'] = True
#                 else:
#                     item['hasBreakfast'] = False
#                 if 14 in line['airEventData']['amenities']:
#                     item['allowsPets'] = True
#                 else:
#                     item['allowsPets'] = False
#                 if 15 in line['airEventData']['amenities']:
#                     item['KidFriendly'] = True
#                 else:
#                     item['KidFriendly'] = False
#                 if 16 in line['airEventData']['amenities']:
#                     item['SuitableforEvents'] = True
#                 else:
#                     item['SuitableforEvents'] = False
#                 if 17 in line['airEventData']['amenities']:
#                     item['SmokingAllowed'] = True
#                 else:
#                     item['SmokingAllowed'] = False
#                 if 18 in line['airEventData']['amenities']:
#                     item['WheelchairAccess'] = True
#                 else:
#                     item['WheelchairAccess'] = False
#                 if 19 in line['airEventData']['amenities']:
#                     item['hasElevator'] = True
#                 else:
#                     item['hasElevator'] = False
#                 if 20 in line['airEventData']['amenities']:
#                     item['hasFireplace'] = True
#                 else:
#                     item['hasFireplace'] = False
#                 if 21 in line['airEventData']['amenities']:
#                     item['hasBuzzer'] = True
#                 else:
#                     item['hasBuzzer'] = False
#                 if 22 in line['airEventData']['amenities']:
#                     item['hasDoorman'] = True
#                 else:
#                     item['hasDoorman'] = False
#                 if 23 in line['airEventData']['amenities']:
#                     item['hasPool'] = True
#                 else:
#                     item['hasPool'] = False
#                 if 24 in line['airEventData']['amenities']:
#                     item['hasHotTub'] = True
#                 else:
#                     item['hasHotTub'] = False
#                 if 25 in line['airEventData']['amenities']:
#                     item['hasGym'] = True
#                 else:
#                     item['hasGym'] = False
#                 if 26 in line['airEventData']['amenities']:
#                     item['has24HrCheckin'] = True
#                 else:
#                     item['has24HrCheckin'] = False
#                 if 30 in line['airEventData']['amenities']:
#                     item['LaptopWorkspace'] = True
#                 else:
#                     item['LaptopWorkspace'] = False
#                 break
#         for metadat in soup('meta'):
#             try:
#                 metadat['property']
#             except KeyError:
#                 continue
#             if 'airbedandbreakfast:locality' in metadat['property']:
#                 item['locality'] = metadat['content']
#             if 'airbedandbreakfast:city' in metadat['property']:
#                 item['city'] = metadat['content']
#             if 'airbedandbreakfast:region' in metadat['property']:
#                 item['region'] = metadat['content']
#             if 'airbedandbreakfast:latitude' in metadat['property']:
#                 item['latitude'] = metadat['content']
#             if 'airbedandbreakfast:longitude' in metadat['property']:
#                 item['longitude'] = metadat['content']
#             break
#         items.append(item)
