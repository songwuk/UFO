# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from ..basic import ReceiverFactory
from .word.wordclient import WordWinCOMReceiver
from .basic import WinCOMReceiverBasic



class COMReceiverFactory(ReceiverFactory):  
    def create_receiver(self, app_root_name: str, process_name: str) -> WinCOMReceiverBasic:
        """
        Create the wincom receiver.
        :param app_root_name: The app root name.
        :param process_name: The process name.
        :return: The receiver.
        """
        win_com_client_mapping = {  
            "WINWORD.EXE": WordWinCOMReceiver  
        }

        com_receiver = win_com_client_mapping.get(app_root_name, None)
        if com_receiver is None:
            raise ValueError(f"Receiver for app root {app_root_name} is not found.")
        

        clsid = self.app_root_mappping(app_root_name)

        if clsid is None:
            raise ValueError(f"App root name {app_root_name} is not supported.")
        
        return com_receiver(app_root_name, process_name)
    

    def app_root_mappping(self, app_root_name:str) -> str:
        """
        Map the app root to the corresponding app.
        :return: The CLSID of the COM object.
        """
        
        win_com_map = {
            "WINWORD.EXE": "Word.Application",
            "EXCEL.EXE": "Excel.Application",
            "POWERPNT.EXE": "PowerPoint.Application",
            "olk.exe": "Outlook.Application"
        }

        return win_com_map.get(app_root_name, None)