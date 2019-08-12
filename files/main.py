"""Desafio Rota Application."""
import sys

"""
   Created At: 10/08/2019
      Contact: jessika.milhomem@gmail.com
"""

def import_file(p_file) :
    file_path = "files/" + p_file
    
    with open(file_path, "r") as file:
        file_treated = [x.strip() for x in file.readlines()]
        file_read = [x.split(",") for x in file_treated]
    
    return file_read


def return_source_list(p_sour_airport, p_l_dataset):
    list_ini = []
    count = 0
    
    while count < len(p_l_dataset):
        if p_l_dataset[count][0] == p_sour_airport:
            list_ini.append(p_l_dataset[count])

        count = count+1
    return list_ini


def return_destination_list(p_dest_airport, p_ini_list, p_l_dataset):
    list_end = []
    count = 0
    while count < len(p_l_dataset):
        if p_l_dataset[count][1] == p_dest_airport:
            if p_l_dataset[count] not in p_ini_list:
                list_end.append(p_l_dataset[count])

        count = count+1
    return list_end



def return_route_list(p_l_middle, p_l_dataset, sour_list, p_prefinal_routes):
    for ini_middle in p_l_middle:
        if ini_middle[0] != "GRU":
            route_list = return_destination_list(ini_middle[0], sour_list, p_l_dataset)
            if route_list:
                p_prefinal_routes.append(route_list[0])
                new_list = return_route_list(route_list, p_l_dataset, sour_list, p_prefinal_routes)
                
    return p_prefinal_routes




def return_prefinal_routes_lists(p_sourcelist, p_destination, p_prefinal_routes):
    list_prefinal_routes = []
    list_prefinal_routes_str = []
    pretotal_value = None
    last_flight = ""    

    for mid in p_prefinal_routes:       
        # se o primeiro item da lista do meio for igual ao segundo item da lista inicial
        if mid[0] == p_sourcelist[len(p_sourcelist)-2]:
            if len(p_sourcelist) == 3:
                #se a lista de prefinais for nula, cria ela
                if not list_prefinal_routes_str:
                    list_prefinal_routes_str.append(p_sourcelist[0])
                    list_prefinal_routes_str.append(p_sourcelist[1])
                    list_prefinal_routes_str.append(mid[1])
                    pretotal_value = int(p_sourcelist[2]) + int(mid[2])

            #senao, apenda novas linhas
            else:
                list_prefinal_routes_str = p_sourcelist
                pretotal_value = p_sourcelist[len(p_sourcelist)-1]
                list_prefinal_routes_str.pop()
                list_prefinal_routes_str.append(mid[1])
                pretotal_value = pretotal_value + int(mid[2]) 
                     
            list_prefinal_routes = list_prefinal_routes_str
            list_prefinal_routes.append(pretotal_value)

            last_flight = mid[1]
    if last_flight != p_destination:
        list_prefinal_routes = return_prefinal_routes_lists(list_prefinal_routes, p_destination, p_prefinal_routes)

    return list_prefinal_routes



def return_cheapest_route(p_list):
    value = 999
    for item in p_list:
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

    
def main(p_argv):
    # Import file
    file = import_file(sys.argv[1])

    # Define the initial and the last destinations
    travel = str(input("Input the source-destination airports desired: "))
    sour_airport = travel[:3]
    dest_airport = travel[4:]
    sour_list = return_source_list(sour_airport, file)
    dest_list = return_destination_list(dest_airport, sour_list, file)  

    route_list = []
    for ini_middle, end_middle, value in dest_list:
        route_list = return_destination_list(ini_middle, sour_list, file)  

    prefinal_routes = []
    prefinal_routes = dest_list + route_list

    middle_list = return_route_list(route_list, file, sour_list, prefinal_routes)
    final_list = []
    aux_list = []
    for ini in sour_list:

        # cria lista final com itens que ja tem o inicio e fim de rota para origem e destino desejados
        if ini[0] == sour_airport and ini[len(ini)-2] == dest_airport:
            final_list.append(ini)

        #se nao, identifica todas as possiveis rotas intermediarias e calcula as rotas inteiras
        else:
            #exclui da lista intermediaria todas as rotas ja finais e faz calculo
            if ini not in final_list:
                aux_list = return_prefinal_routes_lists(ini, dest_airport, prefinal_routes)

            if aux_list:
                final_list.append(aux_list)

    result = return_cheapest_route(final_list)
    print("Cheaper flight ticket:", result)


if __name__ == "__main__":
    result = main(sys.argv)