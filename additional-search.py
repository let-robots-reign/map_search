from geocoder import *
from mapapi import show_map
import sys


def main():
    toponym_to_find = " ".join(sys.argv[1:])
    if toponym_to_find:
        # Поиск по организации
        # Вытаскиваем информацию об организации
        org_name, org_address, org_point, org_hours, delta = get_organization(toponym_to_find, "аптека")
        # Вычисляем координаты введенного объекта
        toponym_coords = get_coordinates(toponym_to_find)
        toponym_point = "{0},{1}".format(toponym_coords[0], toponym_coords[1])
        ll_spn = "ll={0},{1}&spn={2},{3}".format(org_point.split(',')[0], org_point.split(',')[1], delta, delta)
        # Собираем параметры для запроса к StaticMapsAPI:
        # Добавим точки, чтобы указать найденную аптеку и сам объект
        point_param = "pt={0},pm2dgm~{1},pm2rdm".format(org_point, toponym_point)
        # Формируем информационный блок
        print("Имя организации: {}\nАдрес организации: {}\nВремя работы организации: {}"
              "\nДлина пути до организации: {:.2f}".format(org_name, org_address, org_hours,
              lonlat_distance(toponym_point.split(','), org_point.split(','))))
        # Показываем карту
        show_map(ll_spn, "map", add_params=point_param)

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
