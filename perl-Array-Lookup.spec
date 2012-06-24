%include	/usr/lib/rpm/macros.perl
%define	pdir	Array
%define	pnam	Lookup
Summary:	Array::Lookup - lookup strings in arrays or hash tables with abbreviation
Summary(pl):	Array::Lookup - poszukiwanie �a�cuch�w w tablicach lub hashach z u�yciem skr�t�w
Name:		perl-Array-Lookup
Version:	2.1
Release:	2
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1b6441bcf3b1fd8af12dc9d532bc48f2
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.005
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Array::Lookup performs a search through an array of strings, allowing
for abbreviation of the search key. The Lookup subroutine is
especially handy for doing keyword lookups in an array or hash table,
where the keyword may be abbreviated. Exact matches are give priority
over abbreviated matches.

%description -l pl
Modu� Array::Lookup przeszukuje tablic� �a�cuch�w, pozwalaj�c na
skracanie szukanego klucza. Jest wygodny zw�aszcza do wyszukiwania
s��w kluczowych w tablicach zwyk�ych lub haszuj�cych, kiedy s�owa
kluczowe mog� by� skracane. Dok�adne dopasowania maj� wi�kszy
priorytet ni� skr�cone.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
