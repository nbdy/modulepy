from modulepy.Base import Base, Information, Version


class ATestModule(Base):
    information = Information("ATestModule", Version(1, 0, 0))
    dependencies = [Information("GPSDataUser", Version(1, 0, 0))]
