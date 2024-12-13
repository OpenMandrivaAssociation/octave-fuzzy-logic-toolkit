%global octpkg fuzzy-logic-toolkit

Summary:	A mostly MATLAB-compatible fuzzy logic toolkit for Octave
Name:		octave-fuzzy-logic-toolkit
Version:	0.6.1
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/fuzzy-logic-toolkit/
Source0:	https://downloads.sourceforge.net/octave/fuzzy-logic-toolkit-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.2.4

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
A mostly MATLAB-compatible fuzzy logic toolkit for Octave.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

