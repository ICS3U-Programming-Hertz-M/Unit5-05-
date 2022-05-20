#!/usr/bin/env python3

# Created by : Hertz
# Created on : 16, may , 2022
# This program  ask the user to enter there address.


def format_address(
    full_name, ask, street_num, street_name, city, province, postal_code, apt_num=None
):

    # convert from lowercase to capital
    address = (
        full_name.upper()
        + "\n"
        + street_num
        + " "
        + street_name.upper()
        + "\n"
        + city.upper()
        + " "
        + province.upper()
        + " "
        + postal_code.upper()
    )

    # if the user lives in an apartment
    if ask == "y":
        address = (
            full_name.upper()
            + "\n"
            + apt_num
            + "-"
            + street_num
            + " "
            + street_name.upper()
            + "\n"
            + city.upper()
            + " "
            + province.upper()
            + " "
            + postal_code.upper()
        )
    return address


def main():
    apt_num = None

    print("Enter the following and it will return as a Canadian mailing address.")
    print("")

    # get user information
    user_name = input("Full name: ")
    user_ask = input("Do you have an apartment number(y/n)or skip to continue:")

    if user_ask == "y":
        apt_num = input("Apartment number: ")
    user_street_num = input("Street number: ")
    user_street_name = input("Street name: ")
    user_city = input("City: ")
    user_province = input("Province(as an abbreviation," "like ON,Qc,MB etc): ")
    user_postal_code = input("Postal code: ")

    # function call and returned value.
    if apt_num != None:
        address = format_address(
            user_name,
            user_ask,
            user_street_num,
            user_street_name,
            user_city,
            user_province,
            user_postal_code,
            apt_num,
        )

    else:
        address = format_address(
            user_name,
            user_ask,
            user_street_num,
            user_street_name,
            user_city,
            user_province,
            user_postal_code,
        )
    print("")
    print("Your Address is: \n")
    print(address)


if __name__ == "__main__":
    main()
