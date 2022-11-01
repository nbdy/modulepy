from modulepy.Base import Base, Information, Version


class Navigation(Base):
    information = Information("Navigation", Version(1, 0, 0))
    dependencies = [Information("GPS", Version(1, 0, 0))]
