%define short_name	pgpool-ha

Summary:	Pgpool-HA uses heartbeat to keep pgpool from being a single point of failure
Name:		postgresql-%{short_name}
Version:	1.2
Release:	%mkrel 1
License:	BSD
Group:		Databases
URL:		http://pgpool.projects.PostgreSQL.org
Source0:	http://pgfoundry.org/frs/download.php/1124/%{short_name}-%{version}.tar.gz
Patch0:		pgpool-ha-1.2-destdir.patch
Patch1:		pgpool-ha-1.2-pgpool.pid-path.patch
BuildRequires:	heartbeat
Requires:	postgresql-pgpool-II heartbeat
Provides:	%{short_name} = %{version}-%{release}
BuildArch:	noarch

%description
Pgpool-HA combines pgpool with heartbeat. Pgpool is a replication
server of PostgreSQL and makes reliability, but the pgpool server is
always a single point failure.  Pgpool-HA uses heartbeat to eliminate
this.

%prep
%setup -q -n %{short_name}-%{version}
%patch0 -p1 -b .destdir~
%patch1 -p1 -b .pidpath~

%build
%configure2_5x
%make -C src

%install
rm -rf %{buildroot}
%makeinstall_std -C src

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS ChangeLog NEWS
%doc doc/pgpool-ha.en.txt
%lang(ja) %doc doc/pgpool-ha.ja.txt
%{_bindir}/pgpool.monitor
%{_prefix}/lib/ocf/resource.d/heartbeat/pgpool
