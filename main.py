"""Desafio Rota Application."""
import sys
from utils.files_manipulation import *
from cheaper_flight.cheaper_flight import *


def main(p_argv):
    # Import file
    file = import_file(sys.argv[1])

    # Define the initial and the last destinations
    travel = str(input("PLEASE, ENTER DE ROUTE: "))
    sour_airport = travel[:3].upper()
    dest_airport = travel[4:].upper()
    sour_list = return_source_list(sour_airport, file)
    dest_list = return_destination_list(dest_airport, sour_list, file)

    # Define the route possibilities.
    route_list = []
    for ini_middle, end_middle, value in dest_list:
        route_list = return_destination_list(ini_middle, sour_list, file)

    # Create the intermediate route.
    prefinal_routes = []
    prefinal_routes = dest_list + route_list

    middle_list = return_route_list(route_list,
                                    file,
                                    sour_list,
                                    prefinal_routes)

    # Define the final list of routes possibilities
    final_list = []
    aux_list = []
    for ini in sour_list:

        # Define one of final routes,if there is a direct flight
        if ini[0] == sour_airport and ini[len(ini) - 2] == dest_airport:
            final_list.append(ini)

        else:
            if ini not in final_list:
                aux_list = return_prefinal_routes(ini,
                                                  dest_airport,
                                                  prefinal_routes)

            if aux_list:
                final_list.append(aux_list)

    print("\nPOSSIBILITIES:")
    for routes in final_list:
        routes = str(routes)\
                 .replace("[", "")\
                 .replace("]", "")\
                 .replace("'", "")\
                 .replace(",", " - ")
        print(routes, "$")

    # Define and  print the cheapest flight ticket
    result = return_cheapest_route(final_list)
    print(f"\nBEST ROUTE:")
    print(f"{result[0]} > ${result[1]}")


if __name__ == "__main__":
    result = main(sys.argv)
