# (C) Copyright {{ cookiecutter.copyright_year }} {{ cookiecutter.copyright_holder }}.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, {{ cookiecutter.copyright_holder }} does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import {{ cookiecutter.project_slug }}


def test_version() -> None:
    assert {{ cookiecutter.project_slug }}.__version__ != "999"
