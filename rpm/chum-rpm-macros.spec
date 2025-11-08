Name:		chum-rpm-macros
Version:	0.1
Release:	1%{?dist}
Summary:	RPM macros for Sailfish OS Chum

Group:		Development
License:	CC-0
URL:		https://github.com/sailfishos-chum/chum-rpm-macros
#Source0:	%%{name}-%%{version}.tar.gz
Source0:	macros.sailfishos-chum

#BuildRequires:	
#Requires:	

%description


%prep
%setup -q


%build

%install
install -Dpm644 %{S:0} %{buildroot} %{_rpmmacrodir}/macros.sailfishos-chum


%files
%{_rpmmacrodir}/macros.sailfishos-chum

%changelog

