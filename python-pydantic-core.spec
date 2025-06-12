# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pydantic-core
Epoch: 100
Version: 2.35.1
Release: 1%{?dist}
Summary: Core validation logic for pydantic written in rust
License: MIT
URL: https://github.com/pydantic/pydantic-core/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: cargo
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-maturin >= 1.0.0
BuildRequires: python3-pip
BuildRequires: python3-typing-extensions >= 4.6.0
BuildRequires: rust >= 1.64.0

%description
This package provides the core functionality for pydantic validation and
serialization.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pydantic-core
Summary: Core validation logic for pydantic written in rust
Requires: python3
Requires: python3-typing-extensions >= 4.6.0
Provides: python3-pydantic-core = %{epoch}:%{version}-%{release}
Provides: python3dist(pydantic-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pydantic-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pydantic-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pydantic-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pydantic-core) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pydantic-core
This package provides the core functionality for pydantic validation and
serialization.

%files -n python%{python3_version_nodots}-pydantic-core
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pydantic-core
Summary: Core validation logic for pydantic written in rust
Requires: python3
Requires: python3-typing-extensions >= 4.6.0
Provides: python3-pydantic-core = %{epoch}:%{version}-%{release}
Provides: python3dist(pydantic-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pydantic-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pydantic-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pydantic-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pydantic-core) = %{epoch}:%{version}-%{release}

%description -n python3-pydantic-core
This package provides the core functionality for pydantic validation and
serialization.

%files -n python3-pydantic-core
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
