%define		_version	devel
Summary:	Aget - a multithreaded download accelerator
Summary(pl):	Aget - wielow±tkowy akcelerator ¶ci±gania plików
Name:		aget
Version:	0.5
Release:	0.devel.1
License:	Copyrighted by Murat Balaban (distributable, see COPYING)
Group:		Applications
Source0:	http://www.enderunix.org/aget/devel/%{name}-%{_version}.tar.gz
# Source0-md5:	af60e15728a398fb6557f38332440fc6
URL:		http://www.enderunix.org/aget/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aget is a multithreaded download accelerator. The idea behind it is
to implement a console clone of Flashget download manager, a Win32
application that speeds up downloading.

Tests show that Aget is successfull in realizing its objectives. A
file of size 36.347.010 bytes was downloaded in 14 minutes 28 secs
via wget; whereas it was downloaded in 3 minutes and 15 seconds via
aget.

%description -l pl
Aget to wielow±tkowy akcelerator ¶ci±gania plików. G³ówny pomys³
stoj±cy za tym projektem to stworzenie konsolowego klona programu
Flashget znanego z systemu Windows.

Testy pokazuj±, ¿e aget spe³nia postawione wymagania, 36 megabajtowy
plik wget ¶ci±ga³ przez 14 minut 28 sekund, natomiast aget w 3
minuty i 15 sekund.

%prep
%setup -q -n %{name}-%{_version}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags} -pthread"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install aget  $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README* THANKS TODO
%attr(755,root,root) %{_bindir}/aget
