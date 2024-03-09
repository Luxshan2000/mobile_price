import requests
import json 

def test_end_point_test():
    url = "http://127.0.0.1:5000/api/predict"
    data = {
        "columns":['battery_power','blue','clock_speed','dual_sim','fc','four_g','int_memory','m_dep','mobile_wt','n_cores','pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi']
,
        "rows":[[1043,1,1.8,1,14,0,5,0.1,193,3,16,226,1412,3476,12,7,2,0,1,0],
                [841,1,0.5,1,4,1,61,0.8,191,5,12,746,857,3895,6,0,7,1,0,0]]
    }

    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    res = requests.post(url=url,headers=headers,data=data)

    assert res.status_code == 200
    assert res.json()['predictions'] is not None

