from geocoder import *
from mapapi import show_map
import sys


def main():
    toponym_to_find = " ".join(sys.argv[1:])
    if toponym_to_find:
        # Поиск по организации
        # Вытаскиваем информацию об организации
        organizations = get_organization(toponym_to_find, "аптека")
        point_param = "pt="
        for organization in organizations:
            org_name, org_address, org_point, org_hours = organization

            if not org_hours:
                point_param += "{0},pm2grm~".format(org_point)
            if "круглосуточно" in org_hours:
                point_param += "{0},pm2gnm~".format(org_point)
            else:
                point_param += "{0},pm2blm~".format(org_point)

            # # Формируем информационный блок
            # print("Имя организации: {}\nАдрес организации: {}\nВремя работы организации: {}"
            #       "\nДлина пути до организации: {:.2f}\n".format(org_name, org_address, org_hours,
            #       lonlat_distance(toponym_point.split(','), org_point.split(','))))
            # Показываем карту
        point_param = point_param[:-1]
        show_map("map", add_params=point_param)

        # Показываем карту с фиксированным масштабом.
        # lat, lon = get_coordinates(toponym_to_find)
        # ll_spn = "ll={0},{1}&spn=0.005,0.005".format(lat,lon)
        # show_map(ll_spn, "map")
        #
        # Показываем карту с масштабом, подобранным по заданному объекту.
        # ll, spn = get_ll_span(toponym_to_find)
        # ll_spn = "ll={ll}&spn={spn}".format(**locals())
        # point_param = "pt={ll}".format(**locals())
        # show_map(ll_spn, "map", add_params=point_param)
        #
        # Добавляем исходную точку на карту.
        # point_param="pt={ll}".format(**locals())
        # show_map(ll_spn, "map", add_params=point_param)

    else:
        print('No data')


if __name__ == "__main__":
    main()
