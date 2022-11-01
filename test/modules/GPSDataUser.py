from modulepy.Base import Base, Information, Version


class GPSDataUser(Base):
    information = Information("GPSDataUser", Version(1, 0, 0))
    dependencies = [Information("GPS", Version(1, 0, 0))]
