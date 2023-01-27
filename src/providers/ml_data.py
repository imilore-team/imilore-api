from os import environ

import json
from datetime import datetime

from src.init import db
from src.models.ml_data import InMlDiskTableModel, InMlDataModel, OutSmallMlDiskTableModel, OutMlDiskTableModel, OutMlDiskDataModel
from src.tables.ml_data import MlTable, MlData


class MlDataProvider:
    @classmethod
    def add_disk_table(cls, table: InMlDiskTableModel) -> InMlDiskTableModel:
        table_id = db.add(MlTable(title=table.title, description=table.description, db_id=table.disk_id))
        obj = db.get(table_id, MlTable, MlTable.id)

        for data in table.data:
            db.append_childs(object=obj, childs={"data": MlData(
                time=datetime.fromtimestamp(data.time),
                value=data.value,
                error=data.error,
                warn=data.warn
            )})

        return table
    
    @classmethod
    def disk_table_from_json(cls, file) -> InMlDiskTableModel:
        try:
            content = json.load(file)

            data = []
            for values in content["data"]:
                data.append(InMlDataModel(
                    time=int(values["time"]) // 1000, 
                    value=values["value"], 
                    error=values["error"], 
                    warn=values["error"]
                ))

            output = InMlDiskTableModel(
                title=content["title"], 
                description=content["description"],
                disk_id=content["disk_id"],
                data=data
            )

            return output
        except Exception as ex:
            print(ex)
            return InMlDiskTableModel(title="", description="", disk_id="", data=[])

    @classmethod
    def get_all_disks(cls) -> list[OutSmallMlDiskTableModel]:
        output = []
        for item in db.get_all(MlTable):
            output.append(OutSmallMlDiskTableModel(
                id=item.id,
                title=item.title, 
                description=item.description, 
                disk_id=item.db_id
            ))
        return output

    @classmethod
    def get_disk(cls, id: int) -> OutMlDiskTableModel:
        obj = db.get(id, MlTable, MlTable.id)
        data = []
        
        for data_elem in obj.data:
            data.append(OutMlDiskDataModel(
                time=data_elem.time,
                value=data_elem.value,
                error=data_elem.error,
                warn=data_elem.warn
            ))

        return OutMlDiskTableModel(
            id=id,
            title=obj.title,
            description=obj.description,
            disk_id=obj.db_id,
            data=data
        )