from app.core.crud import CRUDBase
from app.models.admin import TotalRecord
from app.schemas.total import TotalRecordCreate, TotalRecordUpdate, TotalRecordYyfsCreate, TotalRecordYyfsUpdate, TotalRecordBsCreate, TotalRecordBsUpdate

class TotalRecordController(CRUDBase[TotalRecord, TotalRecordCreate, TotalRecordUpdate]):
    def __init__(self):
        super().__init__(model=TotalRecord)
        
class TotalRecordYyfsController(CRUDBase[TotalRecord, TotalRecordYyfsCreate, TotalRecordYyfsUpdate]):
    def __init__(self):
        super().__init__(model=TotalRecord)
        
class TotalRecordBsController(CRUDBase[TotalRecord, TotalRecordBsCreate, TotalRecordBsUpdate]):
    def __init__(self):
        super().__init__(model=TotalRecord)

total_record_controller = TotalRecordController()
total_record_yyfs_controller = TotalRecordYyfsController()
total_record_controller_bs = TotalRecordBsController()