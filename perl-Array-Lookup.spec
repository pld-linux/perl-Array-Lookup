#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Array
%define		pnam	Lookup
Summary:	Array::Lookup - lookup strings in arrays or hash tables with abbreviation
Summary(pl.UTF-8):	Array::Lookup - poszukiwanie łańcuchów w tablicach lub hashach z użyciem skrótów
Name:		perl-Array-Lookup
Version:	2.1
Release:	4
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1b6441bcf3b1fd8af12dc9d532bc48f2
URL:		http://search.cpan.org/dist/Array-Lookup/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Array-PrintCols
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Array::Lookup performs a search through an array of strings, allowing
for abbreviation of the search key. The Lookup subroutine is
especially handy for doing keyword lookups in an array or hash table,
where the keyword may be abbreviated. Exact matches are give priority
over abbreviated matches.

%description -l pl.UTF-8
Moduł Array::Lookup przeszukuje tablicę łańcuchów, pozwalając na
skracanie szukanego klucza. Jest wygodny zwłaszcza do wyszukiwania
słów kluczowych w tablicach zwykłych lub haszujących, kiedy słowa
kluczowe mogą być skracane. Dokładne dopasowania mają większy
priorytet niż skrócone.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
