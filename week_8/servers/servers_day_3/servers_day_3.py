
# this is servers day 3 ex.
# it belongs to the crud shape project
# so it is located in ShapManagementProject


import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from shape_manager import ShapeManager


class ShapeItem(BaseModel):
    type: str
    dimensions: list[int]


s1 = ShapeManager()
app = FastAPI()


@app.get("/shapes")
def get_all_shapes():
    """
    :return: all shapes as list of dicts
    """
    shapes_lst = s1.get_all_shapes()
    if not shapes_lst:
        s1.logger.error("shapes list is empty!")
        raise HTTPException(status_code=404, detail="shapes list is empty")
    s1.logger.info("got all shapes")
    return s1.get_all_shapes()


@app.get("/shapes/total-area")
def get_area():
    """
    :return: the sum of area of all shapes
    """
    shapes_obj = s1.shapes
    area = 0.0
    for shape in shapes_obj:
        area += shape.get_area()
    s1.logger.info(f"got area of all shapes | arra = {area}")
    return area


@app.get("/shapes/{shape_id}")
def get_shape(shape_id: int):
    """
    :param shape_id: get the shape id int
    :return: dict of the shape
    """
    shapes_lst = s1.get_all_shapes()
    shape = dict()

    for shape_dct in shapes_lst:
        if shape_dct["id"] == int(shape_id):
            shape =  shape_dct
            break # not necessary. just in case there is 2 obj with the same id
    if not shape:
        message = f"shape {shape_id} not found"
        s1.logger.info(message)
        raise HTTPException(status_code=404, detail=message)
    s1.logger.info("got shapes successfully")
    return shape


@app.post("/shapes")
def add_shape(shape: ShapeItem):
    """
    add shap
    :param shape: dict with type and dimensions
    :return:
    """
    try:
        shape_type = shape.type
        dimensions = shape.dimensions

    # this is from before I used Pydentic
    except KeyError:
        message = f"type or dimensions is missing"
        s1.logger.error(message)
        raise HTTPException(status_code=422, detail=message)

    if not shape_type in ("square", "circle", "rectangle"):
        message = f"shape type {shape_type} is not legal shape"
        s1.logger.error(message)
        raise HTTPException(status_code=422, detail=message)

    shape = {
        "type": shape_type,
        "dimensions": dimensions,
        "id": None
    }
    s1.create_shape(shape)
    s1.logger.info("shape created")
    raise HTTPException(status_code=201, detail=shape)


@app.put("/shapes/{shape_id}")
def update_shape(shape_id, new_shape: dict):
    """
    update the shape in the json
    :param shape_id:
    :param new_shape:
    :return:
    """
    try:
        shape_id = int(shape_id)
        dimensions = new_shape["dimensions"]
        s1.update_shape(shape_id, dimensions)
        raise HTTPException(status_code=200, detail="update success!")
    except KeyError, ValueError, TypeError:
        raise HTTPException(status_code=400, detail="somthing went wrong")


@app.delete("/shapes/{shape_id}")
def delete_shape(shape_id: int):
    """
    deletes shape from the json
    :param shape_id:
    :return:
    """
    try:
        s1.delete_shape(shape_id)
        message = f"shape id {shape_id} was successfully deleted"
        s1.logger.info(message)
        return {"details": message}
    except (ValueError, TypeError) as e:
        s1.logger.error(e)
        raise HTTPException(status_code=404, detail=e)




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)