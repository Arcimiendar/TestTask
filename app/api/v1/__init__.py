from fastapi import APIRouter, Depends
from app.dependencies.db import get_connection
from app.domain.schema import Operation, OperataionInput, OperationOptions, OperationOutput


router = APIRouter()


@router.post('/add', response_model=OperationOutput)
def add_endpoint(operation_input: OperataionInput, conn=Depends(get_connection)):
    operation = Operation(**operation_input.dict(), operation=OperationOptions.add)
    operation_output = operation.calculate_output()
    operation_output.save(conn)
    return operation_output


@router.post('/sub', response_model=OperationOutput)
def sub_endpoint(operation_input: OperataionInput, conn=Depends(get_connection)):
    operation = Operation(**operation_input.dict(), operation=OperationOptions.sub)
    operation_output = operation.calculate_output()
    operation_output.save(conn)
    return operation_output


@router.post('/div', response_model=OperationOutput)
def div_endpoint(operation_input: OperataionInput, conn=Depends(get_connection)):
    operation = Operation(**operation_input.dict(), operation=OperationOptions.div)
    operation_output = operation.calculate_output()
    operation_output.save(conn)
    return operation_output


@router.post('/mul', response_model=OperationOutput)
def mul_endpoint(operation_input: OperataionInput, conn=Depends(get_connection)):
    operation = Operation(**operation_input.dict(), operation=OperationOptions.mul)
    operation_output = operation.calculate_output()
    operation_output.save(conn)
    return operation_output
