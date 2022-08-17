def test_sum_endoint(client, db):
    """
    Test operation succed, record in DB and output object is correct
    """
    test_obj = {'left_operand': 12, 'right_operand': 33, 'result': 45}
    response = client.request(
        'POST', '/api/v1/add',
        json=test_obj
    )
    assert response.status_code == 200
    with db.cursor() as curs:
        curs.execute("""
            SELECT left_operand, right_operand, result
            FROM calculation_result
            WHERE left_operand = %s AND right_operand = %s AND result = %s;
        """, (test_obj['left_operand'], test_obj['right_operand'], test_obj['result']))
        data = curs.fetchall()
    assert data and data[0], 'No record in DB'
    out_obj = response.json()
    assert out_obj['left_operand'] == test_obj['left_operand']
    assert out_obj['right_operand'] == test_obj['right_operand']
    assert out_obj['result'] == test_obj['result']


def test_div_endoint(client, db):
    """
    Test operation succed, record in DB and output object is correct
    """
    test_obj = {'left_operand': 12, 'right_operand': 4, 'result': 3}
    response = client.request(
        'POST', '/api/v1/div',
        json=test_obj
    )
    assert response.status_code == 200
    with db.cursor() as curs:
        curs.execute("""
            SELECT left_operand, right_operand, result
            FROM calculation_result
            WHERE left_operand = %s AND right_operand = %s AND result = %s;
        """, (test_obj['left_operand'], test_obj['right_operand'], test_obj['result']))
        data = curs.fetchall()
    assert data and data[0], 'No record in DB'
    out_obj = response.json()
    assert out_obj['left_operand'] == test_obj['left_operand']
    assert out_obj['right_operand'] == test_obj['right_operand']
    assert out_obj['result'] == test_obj['result']


def test_div_endpoint_failed(client, db):
    """
    Test operation failed, record is not in DB
    """
    test_obj = {'left_operand': 12, 'right_operand': 0}
    response = client.request(
        'POST', '/api/v1/div',
        json=test_obj
    )
    assert response.status_code == 422
    with db.cursor() as curs:
        curs.execute("""
            SELECT left_operand, right_operand, result
            FROM calculation_result
            WHERE left_operand = %s AND right_operand = %s;
        """, (test_obj['left_operand'], test_obj['right_operand']))
        data = curs.fetchall()
    assert not data, 'Record should not be in DB'


def test_sub_endoint(client, db):
    """
    Test operation succed, record in DB and output object is correct
    """
    test_obj = {'left_operand': 12, 'right_operand': 33, 'result': -21}
    response = client.request(
        'POST', '/api/v1/sub',
        json=test_obj
    )
    assert response.status_code == 200
    with db.cursor() as curs:
        curs.execute("""
            SELECT left_operand, right_operand, result
            FROM calculation_result
            WHERE left_operand = %s AND right_operand = %s AND result = %s;
        """, (test_obj['left_operand'], test_obj['right_operand'], test_obj['result']))
        data = curs.fetchall()
    assert data and data[0], 'No record in DB'
    out_obj = response.json()
    assert out_obj['left_operand'] == test_obj['left_operand']
    assert out_obj['right_operand'] == test_obj['right_operand']
    assert out_obj['result'] == test_obj['result']


def test_mul_endoint(client, db):
    """
    Test operation succed, record in DB and output object is correct
    """
    test_obj = {'left_operand': 5, 'right_operand': 3, 'result': 15}
    response = client.request(
        'POST', '/api/v1/mul',
        json=test_obj
    )
    assert response.status_code == 200
    with db.cursor() as curs:
        curs.execute("""
            SELECT left_operand, right_operand, result
            FROM calculation_result
            WHERE left_operand = %s AND right_operand = %s AND result = %s;
        """, (test_obj['left_operand'], test_obj['right_operand'], test_obj['result']))
        data = curs.fetchall()
    assert data and data[0], 'No record in DB'
    out_obj = response.json()
    assert out_obj['left_operand'] == test_obj['left_operand']
    assert out_obj['right_operand'] == test_obj['right_operand']
    assert out_obj['result'] == test_obj['result']
