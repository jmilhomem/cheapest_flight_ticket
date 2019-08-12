"""Desafio Rota Application."""
import sys
from utils.files_manipulation import *
from cheaper_flight.cheaper_flight import *


def main(p_argv):
    # Import file
    file = import_file(sys.argv[1])

    # Define the initial and the last destinations
    travel = str(input("Input the source-destination airports desired: "))
    sour_airport = travel[:3]
    dest_airport = travel[4:]
    sour_list = return_source_list(sour_airport, file)
    dest_list = return_destination_list(dest_airport, sour_list, file)  

    # Define the route possibilities.
    route_list = []
    for ini_middle, end_middle, value in dest_list:
        route_list = return_destination_list(ini_middle, sour_list, file)  

    # Create the prefinal route.
    prefinal_routes = []
    prefinal_routes = dest_list + route_list
    middle_list = return_route_list(route_list, file, sour_list, prefinal_routes)
    
    #Define the list of possibilities
    final_list = []
    aux_list = []
    for ini in sour_list:

        if ini[0] == sour_airport and ini[len(ini)-2] == dest_airport:
            final_list.append(ini)

        else:
            if ini not in final_list:
                aux_list = return_prefinal_routes_lists(ini, dest_airport, prefinal_routes)

            if aux_list:
                final_list.append(aux_list)

    #Define and  print the cheapest flight ticket
    result = return_cheapest_route(final_list)
    print("Cheaper flight ticket:", result)


if __name__ == "__main__":
    result = main(sys.argv)