from modulepy.ModuleBase import ModuleBase, ModuleInformation, ModuleVersion, SharedData


class GPSDataUser(ModuleBase):
    information = ModuleInformation("GPSDataUser", ModuleVersion(1, 0, 0))
    dependencies = [
        ModuleInformation("GPS", ModuleVersion(1, 0, 0))
    ]

    def process_input_data(self, data: SharedData):
        if data.origin.name == "GPS":
            print("GPSDataReceiver:", data.data)
