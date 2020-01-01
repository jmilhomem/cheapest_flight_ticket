"""Route Challenge Application."""
import sys
from utils.files_manipulation import import_file
from cheaper_flight.cheaper_flight import return_source_list
from cheaper_flight.cheaper_flight import return_destination_list
from cheaper_flight.cheaper_flight import return_prefinal_routes
from cheaper_flight.cheaper_flight import return_cheapest_route


def main(filename):
    """Main function to call the program."""
    stop_defined = ""
    while stop_defined.lower() != "yes":
        execute_app(filename)
        stop_defined = input("\nDO YOU WANT TO QUIT? (YES/NO): ")


def execute_app(filename):
    """Function to execute the program."""
    file = import_file(filename)

    # Define the initial and the last destinations
    travel = str(input("PLEASE, ENTER DE ROUTE: "))
    sour_airport = travel[:3].upper()
    dest_airport = travel[4:].upper()
    sour_list = return_source_list(sour_airport, file)
    dest_list = return_destination_list(dest_airport, sour_list, file)

    try:
        # Define the route possibilities.
        route_list = []
        for ini_middle, end_middle, value in dest_list:
            route_list = return_destination_list(ini_middle, sour_list, file)

        # Create the intermediate route.
        prefinal_routes = []
        prefinal_routes = dest_list + route_list

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
        print("\nBEST ROUTE:")
        print("{} > ${}".format(result[0], result[1]))

    except UnboundLocalError:
        print("Please, check the route informed. Anyone not exist in file!")


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
