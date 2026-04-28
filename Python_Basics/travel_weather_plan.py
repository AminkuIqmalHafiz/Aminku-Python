distance_mi = 300
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = False


if distance_mi == 0:
    print (False)

elif distance_mi <= 1 :
    if is_raining == False :
        print (True)
    else:
        print (False)

elif 1 >= distance_mi <= 6 :
    if has_bike == True and is_raining == False:
        print (True)
    else:
        print (False)


elif distance_mi >= 6 :
    if has_car == True or has_ride_share_app == True:
        print (True)
    else:
        print (False)
