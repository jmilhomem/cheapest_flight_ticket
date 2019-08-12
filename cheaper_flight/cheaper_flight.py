"""Cheaper Flight module."""
import sys


def return_source_list(p_source, p_dataset):
    """
    Return the list with all sources informed.

    param p_source:  the source informed
    param p_dataset:  list with the dataset
    return: a list with all sources routes
    """
    list_ini = []
    count = 0
    
    while count < len(p_dataset):
        if p_dataset[count][0] == p_source:
            list_ini.append(p_dataset[count])

        count = count+1
    return list_ini


def return_destination_list(p_destination, p_source, p_dataset):
    """
    Return the list with all destinations informed.

    param p_destination:  the destination informed
    param p_source: the source list
    param p_dataset:  list with the dataset
    return: a list with all destinations routes
    """
    dest_list = []
    count = 0
    while count < len(p_dataset):
        if p_dataset[count][1] == p_destination:
            if p_dataset[count] not in p_source:
                dest_list.append(p_dataset[count])

        count = count+1
    return dest_list


def return_route_list(p_routes, p_dataset, p_source, p_prefinal_routes):
    """
    Return the route list with all destinations informed.

    param p_routes:  the routes possibles list
    param p_dataset:  list with the dataset
    param p_source: the source list
    param p_prefinal_routes: the prefinal list with all possible routes
    return: a list with all routes
    """
    for ini_middle in p_routes:
        if ini_middle[0] != "GRU":
            route_list = return_destination_list(ini_middle[0], p_source, p_dataset)
            if route_list:
                p_prefinal_routes.append(route_list[0])
                new_list = return_route_list(route_list, p_dataset, p_source, p_prefinal_routes)
                
    return p_prefinal_routes


def return_prefinal_routes_lists(p_source, p_destination, p_prefinal_routes):
    """
    Return the prefinal list with all destinations informed.

    param p_source: the source list
    param p_destination:  the destination informed
    param p_prefinal_routes: the prefinal list with all possible routes
    return: a list with all prefinal routes
    """
    list_prefinal_routes = []
    list_prefinal_routes_str = []
    pretotal_value = None
    last_flight = ""    

    for mid in p_prefinal_routes:       
        # if the route has other paths, create the datasets
        #print("2", mid, p_source, p_destination)

        if mid[0] == p_source[len(p_source)-2]:
            if len(p_source) == 3:
                #se a lista de prefinais for nula, cria ela
                if not list_prefinal_routes_str:
                    list_prefinal_routes_str.append(p_source[0])
                    list_prefinal_routes_str.append(p_source[1])
                    list_prefinal_routes_str.append(mid[1])
                    pretotal_value = int(p_source[2]) + int(mid[2])

            #append new data
            else:
                list_prefinal_routes_str = p_source
                pretotal_value = p_source[len(p_source)-1]
                list_prefinal_routes_str.pop()
                list_prefinal_routes_str.append(mid[1])
                pretotal_value = pretotal_value + int(mid[2]) 
                     
            list_prefinal_routes = list_prefinal_routes_str
            list_prefinal_routes.append(pretotal_value)

            last_flight = mid[1]
    if last_flight != p_destination:
        list_prefinal_routes = return_prefinal_routes_lists(list_prefinal_routes, p_destination, p_prefinal_routes)

    return list_prefinal_routes


def return_cheapest_route(p_routes):
    """
    Return the cheapest flight ticket

    param p_routes: the routes list
    return: a list with the chepeast fligth ticket
    """
    value = 999
    if p_routes:
        for item in p_routes:
            if float(item[len(item)-1]) < float(value):
                value = item[len(item)-1]
                item_result = item
                item_result.pop()
                route = str(item_result) \
                        .replace("[", "") \
                        .replace("]", "") \
                        .replace(",", "") \
                        .replace("'", "") \
                        .replace(" ", " - ")
    return route
