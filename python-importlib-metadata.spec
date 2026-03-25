%define module	importlib-metadata
%define oname importlib_metadata

Name:		python-importlib-metadata
Summary:	Library to access the metadata for a Python package
Version:	9.0.0
Release:	1
Group:		Development/Python
License:	Apache-2.0
URL:		https://github.com/python/importlib_metadata
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(tomli)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(zipp)

%description
importlib_metadata is a library which provides an API for accessing an
installed package’s metadata (see PEP 566), such as its entry points or
its top-level name.

This functionality intends to replace most uses of pkg_resources entry
point API and metadata API.

Along with importlib.resources in Python 3.7 and newer (backported as
importlib_resources for older versions of Python), this can eliminate
the need to use the older and less efficient pkg_resources package.

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"

%files
%doc README.rst NEWS.rst
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
