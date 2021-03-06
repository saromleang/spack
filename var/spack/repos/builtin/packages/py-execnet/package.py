##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class PyExecnet(PythonPackage):
    """execnet provides a share-nothing model with channel-send/receive
    communication for distributing execution across many Python interpreters
    across version, platform and network barriers."""

    homepage = "http://codespeak.net/execnet"
    url      = "https://pypi.io/packages/source/e/execnet/execnet-1.4.1.tar.gz"

    version('1.4.1', '0ff84b6c79d0dafb7e2971629c4d127a')

    depends_on('py-setuptools',  type='build')
    depends_on('py-setuptools-scm',  type='build')
    depends_on('py-apipkg@1.4:', type=('build', 'run'))
