class checkAdjacency_:
    # def __init__(self):
    #     pass

    def get_geom(self,geomPool):
        # """
        # gets the selected parcel geometries
        # :param geomPool:
        # :return: will return boolian values
        # """
        lst_identified_adjacency= []
        for i in geomPool:
            # will append boolian values by checking their adjacency
            lst_ = []
            for j in geomPool:
                if j != i:
                    lst_.append(j)
            adjacency_ = self.checkgeom(i, lst_)
            lst_identified_adjacency.append(adjacency_)
        if False in lst_identified_adjacency:
            # check for touches geometry functionality

            return  False
        else:
            return True

    def checkgeom(self, trimmedGeom, restofGeom):
        # """
        # will check if the geometry is adjacent
        # :param trimmedGeom:
        # :param restofGeom:
        # :return: true if they are adjacent or false if they are not
        # """
        adjacency = False
        for i in trimmedGeom[0]:
            for g in restofGeom:
                if i in g[0]:
                    adjacency = True
        return adjacency
