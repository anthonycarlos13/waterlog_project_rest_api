__author__ = 'anthonymendoza'

from bs4 import BeautifulSoup
from django.apps import apps
import requests

reservoir_model = apps.get_model('water_store', 'Reservoir')


def aggregate_scraped_data():
    station_meta_data = {}
    station_time_series_data = {}
    station_id_inventory = ['ORO', 'CLE', 'LEW', 'WHI', 'ANT',
                            'SHA', 'KES', 'DAV', 'BUL', 'WRS',
                            'FOL', 'UNV', 'LON', 'INV', 'CAS'
                            'BLB', 'NHG', 'CMN', 'PAR', 'DON',
                            'BRD', 'TUL', 'NML', 'HTH', 'CHV',
                            'BUC', 'HID', 'MIL', 'SNL', 'PNF',
                            'TRM', 'SCC', 'ISB', 'STP', 'DNN',
                            'PYM']

    try:
        for station_id in station_id_inventory:
            station_meta_data[station_id] = scrape_meta_data(station_id)
            station_time_series_data[station_id] = scrape_timeseries_data(station_id, station_meta_data[station_id])
    except Exception as e:
        pass

    return station_time_series_data


def scrape_meta_data(station_id):
    swp_client_request_meta_data = requests.get('http://cdec.water.ca.gov/cgi-progs/profile?s=%s&type=dam' % station_id)
    request_soupified = BeautifulSoup(swp_client_request_meta_data.text, "html.parser")

    meta_data_fields = {
        "dam name": None,
        "dam_id": station_id,
        "national id": None,
        "reservoir area": None,
        "latitude": None,
        "longitude": None,
        "county": None,
        "stream": None,
        "storage capacity": None,
        "material volume": None,
    }
    td_list = request_soupified.find_all(lambda tag: tag.name == 'td' and tag.string is not None)

    for td in td_list:
        if td.string.lower() in meta_data_fields:
            try:
                num = float(''.join(y for y in td.string.next.string if y.isdigit() or y == '.' or y == ','))
                meta_data_fields[td.string.lower()] = num
            except ValueError:
                meta_data_fields[td.string.lower()] = td.string.next.string.lower()
    return meta_data_fields.copy()


def scrape_timeseries_data(station_id, meta_data):
    swp_client_request_meta_data = requests.get(
        'http://cdec.water.ca.gov/cgi-progs/queryDaily?%s&d=11-Nov-2016+09:35&span=365days' % station_id)
    request_soupified = BeautifulSoup(swp_client_request_meta_data.text, "html.parser")
    td_list = request_soupified.find_all('td')
    station_calls = {
        'ORO': ORO(td_list, meta_data),
        'CLE': CLE(td_list, meta_data),
        'LEW': LEW(td_list, meta_data),
        'WHI': WHI(td_list, meta_data),
        'ANT': ANT(td_list, meta_data),
        'WRS': WRS(td_list, meta_data),
        'SHA': SHA(td_list, meta_data),
        'KES': KES(td_list, meta_data),
        'DAV': DAV(td_list, meta_data),
        'BUL': BUL(td_list, meta_data),
        'ENG': ENG(td_list, meta_data),
        'FOL': FOL(td_list, meta_data),
        'UNV': UNV(td_list, meta_data),
        'LON': LON(td_list, meta_data),
        'INV': INV(td_list, meta_data),
        'BLB': BLB(td_list, meta_data),
        'NHG': NHG(td_list, meta_data),
        'CMN': CMN(td_list, meta_data),
        'PAR': PAR(td_list, meta_data),
        'DON': DON(td_list, meta_data),
        'BRD': BRD(td_list, meta_data),
        'TUL': TUL(td_list, meta_data),
        'NML': NML(td_list, meta_data),
        'HTH': HTH(td_list, meta_data),
        'CHV': CHV(td_list, meta_data),
        'BUC': BUC(td_list, meta_data),
        'HID': HID(td_list, meta_data),
        'MIL': MIL(td_list, meta_data),
        'SNL': SNL(td_list, meta_data),
        'PNF': PNF(td_list, meta_data),
        'TRM': TRM(td_list, meta_data),
        'SCC': SCC(td_list, meta_data),
        'ISB': ISB(td_list, meta_data),
        'STP': STP(td_list, meta_data),
        'DNN': DNN(td_list, meta_data),
        'PYM': PYM(td_list, meta_data),
        'CAS': CAS(td_list, meta_data),
        'PRR': PAR(td_list, meta_data)

    }
    return station_calls[station_id]


def ORO(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=75, count_start=50, intervals=25, re_target=1,
                       rs_target=3, o_target=11,
                       i_target=13, pi_target=19,
                       pa_target=21)


def CLE(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=138, count_start=92, intervals=23, re_target=1,
                       rs_target=3, o_target=7,
                       i_target=9, pi_target=17,
                       pa_target=None)


def LEW(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=57, count_start=38, intervals=19, re_target=1,
                       rs_target=3, o_target=7,
                       i_target=9, pi_target=None,
                       pa_target=None)


def WHI(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=69, count_start=46, intervals=23, re_target=1,
                       rs_target=3, o_target=7,
                       i_target=9, pi_target=15,
                       pa_target=None)


def ANT(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=51, count_start=34, intervals=17, re_target=1,
                       rs_target=3,
                       o_target=None, i_target=None, pi_target=7,
                       pa_target=9)


def WRS(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=69, count_start=46, intervals=23, re_target=1,
                       rs_target=3, o_target=11, i_target=13, pi_target=15,
                       pa_target=None)


def SHA(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=87, count_start=58, intervals=29, re_target=1,
                       rs_target=3, o_target=11, i_target=13, pi_target=21,
                       pa_target=23)


def KES(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=33, count_start=22, intervals=11, re_target=1,
                       rs_target=3, o_target=7, i_target=9, pi_target=None,
                       pa_target=None)


def DAV(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=33, count_start=22, intervals=11, re_target=1,
                       rs_target=3, o_target=None, i_target=None, pi_target=7,
                       pa_target=9)


def BUL(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=33, count_start=22, intervals=11, re_target=1,
                       rs_target=3, o_target=None, i_target=None, pi_target=None,
                       pa_target=None)


def ENG(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=39, count_start=26, intervals=13, re_target=1,
                       rs_target=3, o_target=None, i_target=9, pi_target=11,
                       pa_target=None)


def FOL(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=87, count_start=58, intervals=29, re_target=1,
                       rs_target=3, o_target=11, i_target=13, pi_target=21,
                       pa_target=None)


def UNV(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=21, count_start=14, intervals=7, re_target=1,
                       rs_target=3, o_target=None, i_target=None, pi_target=None,
                       pa_target=None)


def LON(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=51, count_start=34, intervals=17, re_target=1,
                       rs_target=3, o_target=None, i_target=None, pi_target=7,
                       pa_target=9)


def INV(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=45, count_start=30, intervals=15, re_target=1,
                       rs_target=3, o_target=9, i_target=11, pi_target=13,
                       pa_target=None)


def BLB(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=69, count_start=46, intervals=23, re_target=1, rs_target=3, o_target=11, i_target=13, pi_target=15,
                   pa_target=None)


def NHG(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=69, count_start=46, intervals=23, re_target=1, rs_target=3, o_target=11, i_target=13, pi_target=17,
                   pa_target=None)


def CMN(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=45, count_start=30, intervals=15, re_target=1, rs_target=3, o_target=11, i_target=13, pi_target=None,
                   pa_target=None)


def PAR(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=39, count_start=26, intervals=13, re_target=1, rs_target=3, o_target=7, i_target=9, pi_target=11,
                   pa_target=None)


def DON(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=21, count_start=14, intervals=7, re_target=1, rs_target=None, o_target=5, i_target=None, pi_target=None,
                   pa_target=None)


def BRD(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=27, count_start=18, intervals=9, re_target=None, rs_target=1, o_target=5, i_target=None, pi_target=7,
                   pa_target=None)


def TUL(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=69, count_start=46, intervals=23, re_target=1, rs_target=3, o_target=11, i_target=13, pi_target=None,
                   pa_target=None)


def NML(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=81, count_start=54, intervals=27, re_target=1, rs_target=3, o_target=11, i_target=13, pi_target=21,
                   pa_target=None)


def HTH(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=51, count_start=34, intervals=17, re_target=None, rs_target=3, o_target=7, i_target=None, pi_target=11,
                   pa_target=13)


def CHV(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=27, count_start=18, intervals=9, re_target=None, rs_target=1, o_target=5, i_target=None, pi_target=7,
                   pa_target=None)


def BUC(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=63, count_start=42, intervals=21, re_target=1, rs_target=3, o_target=11, i_target=13, pi_target=None,
                   pa_target=None)


def HID(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=75, count_start=50, intervals=25, re_target=1, rs_target=3, o_target=11, i_target=13, pi_target=15,
                   pa_target=None)


def MIL(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=75, count_start=50, intervals=25, re_target=1, rs_target=3, o_target=11, i_target=13, pi_target=21,
                   pa_target=None)


def SNL(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=21, count_start=14, intervals=7, re_target=1, rs_target=3, o_target=None, i_target=None, pi_target=None,
                   pa_target=None)


def PNF(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=87, count_start=58, intervals=29, re_target=1, rs_target=3, o_target=11, i_target=13, pi_target=17,
                   pa_target=None)


def TRM(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=81, count_start=54, intervals=27, re_target=1, rs_target=3, o_target=11, i_target=13, pi_target=17,
                   pa_target=None)


def SCC(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=87, count_start=58, intervals=29, re_target=1, rs_target=3, o_target=11, i_target=13, pi_target=17,
                   pa_target=None)


def ISB(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=87, count_start=58, intervals=29, re_target=1, rs_target=3, o_target=11, i_target=13, pi_target=17,
                   pa_target=None)


def STP(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=33, count_start=22, intervals=11, re_target=1, rs_target=3, o_target=None, i_target=None, pi_target=None,
                   pa_target=None)


def DNN(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=21, count_start=14, intervals=7, re_target=1, rs_target=3, o_target=None, i_target=None, pi_target=None,
                   pa_target=None)


def PYM(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=21, count_start=14, intervals=7, re_target=1, rs_target=3, o_target=None, i_target=None, pi_target=None,
                   pa_target=None)


def CAS(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=21, count_start=14, intervals=7, re_target=1, rs_target=3, o_target=None, i_target=None, pi_target=None,
                   pa_target=None)


def PRR(td_list, meta_data):
    return scraper_algorithm(meta_data=meta_data, td_list=td_list, switch=27, count_start=18, intervals=9, re_target=1, rs_target=3, o_target=None, i_target=None, pi_target=7,
                   pa_target=None)


def scraper_algorithm(meta_data, td_list, switch, count_start, intervals, re_target, rs_target, o_target, i_target, pi_target,
                pa_target):
    time_series_data = []
    data_fields = {
        "date": None,
        "reservoir elevation": None,
        "reservoir storage": None,
        "outflow": None,
        "inflow": None,
        "precipitation incremental": None,
        "precipitation accumulated": None,
        "name": None,
        "id": None,
        "national_id": None,
        "reservoir_area": None,
        "latitude": None,
        "longitude": None,
        "county": None,
        "stream": None,
        "storage_capacity": None
    }

    count = 0
    res_elev_target = 0
    res_storage_target = 0
    outflow_target = 0
    inflow_target = 0
    precip_inc_target = 0
    precip_acc_target = 0

    for td in td_list:
        if count < count_start:
            count += 1
            continue
        else:
            if (count % intervals) == 0:
                if count == switch:
                    data_fields['name'] = meta_data['dam name']
                    data_fields['id'] = meta_data['dam_id']
                    data_fields['reservoir_area'] = meta_data['reservoir area']
                    data_fields['latitude'] = meta_data['latitude']
                    data_fields['longitude'] = meta_data['longitude']
                    data_fields['county'] = meta_data['county']
                    data_fields['stream'] = meta_data['stream']
                    data_fields['storage_capacity'] = meta_data['storage capacity']
                    time_series_data.append(data_fields.copy())
                    switch += intervals
                data_fields["date"] = td.string.strip() if td.string is not None else None
                res_elev_target = None if re_target is None else count + re_target
                res_storage_target = None if rs_target is None else count + rs_target
                outflow_target = None if o_target is None else count + o_target
                inflow_target = None if i_target is None else count + i_target
                precip_inc_target = None if pi_target is None else count + pi_target
                precip_acc_target = None if pa_target is None else count + pa_target
            else:
                if count == res_elev_target:
                    data_fields["reservoir elevation"] = td.string.strip() if td.string is not None else None
                elif count == res_storage_target:
                    data_fields["reservoir storage"] = td.string.strip() if td.string is not None else None
                elif count == outflow_target:
                    data_fields["outflow"] = td.string.strip() if td.string is not None else None
                elif count == inflow_target:
                    data_fields["inflow"] = td.string.strip() if td.string is not None else None
                elif count == precip_inc_target:
                    data_fields["precipitation incremental"] =td.string.strip() if td.string is not None else None
                elif count == precip_acc_target:
                    data_fields["precipitation accumulated"] = td.string.strip() if td.string is not None else None
                else:
                    pass
            count += 1
    return time_series_data
