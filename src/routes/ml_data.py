from fastapi import APIRouter, UploadFile

from src.models.ml_data import InMlDiskTableModel, OutSmallMlDiskTableModel, OutMlDiskTableModel
from src.providers.ml_data import MlDataProvider


router = APIRouter(prefix="/data")


@router.post("/send_disk")
def post_send_data(table: InMlDiskTableModel) -> bool:
    MlDataProvider.add_disk_table(table)
    return True

@router.post("/send_disk_file")
def post_send_file_data(file: UploadFile) -> bool:
    MlDataProvider.add_disk_table(MlDataProvider.disk_table_from_json(file.file))
    return True


@router.get("/get_all_disks")
def get_all_disks_data() -> list[OutSmallMlDiskTableModel]:
    return MlDataProvider.get_all_disks()

@router.get("/get_disk")
def get_disk_data(id: int) -> OutMlDiskTableModel:
    return MlDataProvider.get_disk(id)