# -*- coding: utf-8 -*-
"""
/***************************************************************************
 checkAdjacency
                                 A QGIS plugin
 This plugin checks adjacency of selected features
                             -------------------
        begin                : 2017-02-03
        copyright            : (C) 2017 by Mael Taye ,INSA
        email                : mael.taye@insa.gov.et
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load checkAdjacency class from file checkAdjacency.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .adjacency_checker import checkAdjacency
    return checkAdjacency(iface)
