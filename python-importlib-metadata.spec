%define pypi_name	importlib-metadata

Name:		python-%{pypi_name}
Summary:	Library to access the metadata for a Python package.
Version:	8.7.0
Release:	1
Group:		Development/Python
License:	Apache 2.0
URL:		https://github.com/python/importlib_metadata
Source0:	https://github.com/python/importlib_metadata/archive/refs/tags/v%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{py_ver}dist(setuptools)
BuildRequires:	python%{py_ver}dist(setuptools-scm)
BuildRequires:  python%{py_ver}dist(pip)
BuildRequires:  python%{py_ver}dist(zipp)
BuildRequires:	python%{py_ver}dist(tomli)
BuildRequires:	python-pip
BuildRequires:	python-wheel

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
importlib_metadata is a library which provides an API for accessing an installed package’s metadata (see PEP 566), such as its entry points or its top-level name.
This functionality intends to replace most uses of pkg_resources entry point API and metadata API. 
Along with importlib.resources in Python 3.7 and newer (backported as importlib_resources for older versions of Python), 
this can eliminate the need to use the older and less efficient pkg_resources package.

%prep
%autosetup -p1 -n importlib_metadata-%{version}

# drop bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
mkdir wheels
pip wheel --wheel-dir wheels --no-deps --no-build-isolation --verbose .

%install
pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links wheels wheels/*.whl

%files
%doc README.rst CHANGES.rst
%{python_sitelib}/*dist-info
%{python_sitelib}/importlib_metadata
