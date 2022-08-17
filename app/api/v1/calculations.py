from fastapi import APIRouter, Depends
from app.dependencies.db import get_connection
from app.domain.schema import Operation, OperataionInput, OperationOptions, OperationOutput


router = APIRouter()


@router.post('/add', response_model=OperationOutput)
def add_endpoint(operation_input: OperataionInput, conn=Depends(get_connection)):
    """
    This endpoint performs operation "add".
    I've decided to write all 4 endpoints separetly, because otherwise application will contain 1 endpoint only,
    and I thought it may be not interesting enough.
    It would be better to "unify" them in real life. Besides, enum will be shown in open-api
    :param operation_input: user provided data with all operands
    :param conn: db connection
    :return: result of computation
    """
    operation = Operation(**operation_input.dict(), operation=OperationOptions.add)
    operation_output = operation.calculate_output()
    operation_output.save(conn)
    return operation_output


@router.post('/sub', response_model=OperationOutput)
def sub_endpoint(operation_input: OperataionInput, conn=Depends(get_connection)):
    """
    This endpoint performs operation "sub".
    :param operation_input: user provided data with all operands
    :param conn: db connection
    :return: result of computation
    """
    operation = Operation(**operation_input.dict(), operation=OperationOptions.sub)
    operation_output = operation.calculate_output()
    operation_output.save(conn)
    return operation_output


@router.post('/div', response_model=OperationOutput)
def div_endpoint(operation_input: OperataionInput, conn=Depends(get_connection)):
    """
    This endpoint performs operation "div".
    :param operation_input: user provided data with all operands
    :param conn: db connection
    :return: result of computation
    """
    operation = Operation(**operation_input.dict(), operation=OperationOptions.div)
    operation_output = operation.calculate_output()
    operation_output.save(conn)
    return operation_output


@router.post('/mul', response_model=OperationOutput)
def mul_endpoint(operation_input: OperataionInput, conn=Depends(get_connection)):
    """
    This endpoint performs operation "mul".
    :param operation_input: user provided data with all operands
    :param conn: db connection
    :return: result of computation
    """
    operation = Operation(**operation_input.dict(), operation=OperationOptions.mul)
    operation_output = operation.calculate_output()
    operation_output.save(conn)
    return operation_output
