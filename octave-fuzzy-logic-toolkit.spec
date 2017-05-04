%define octpkg fuzzy-logic-toolkit

Summary:	A mostly MATLAB-compatible fuzzy logic toolkit for Octave
Name:		octave-%{octpkg}
Version:	0.4.5
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.2.4

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
A mostly MATLAB-compatible fuzzy logic toolkit for Octave.

This package is part of community Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}/NEWS
%doc %{octpkg}/COPYING

