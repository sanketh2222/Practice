age_year=input("Enter your inp.")
if len(age_year)==4:
    if int(age_year)>2020:
        print("you are not born yet")
    else:
        print("you entered year")
        age=int(age_year)+100
        if 2020-int(age_year)>=150:
            print("you seem to be very old")
            year = int(input("enter year"))
            age = year - int(age_year)
            print(f"you will be {age} in year {year} ")
        else:
            print(f"you will be 100 in {age}")
            year=int(input("enter year"))
            age=year-int(age_year)
            print(f"you will be {age} in year {year} ")
else:
    if int(age_year)==0:
        print("min age should be 1")
    elif int(age_year)>=150:
        print("you seem to be very old")
        exit(0)
        # year = int(input("enter year"))
        # age=year-(2020-int(age_year))
        # print(f"you will be {age} in year {year}")
    else:
        print("you entered your age")
        year=2020+100-int(age_year)
        print(f"you will be 100 in {year} ")
        year=int(input("enter year"))
        age=year-(2020-int(age_year))
        print(f"you will be {age} in year {year}")