Summary:	The media9 LaTeX package
Summary(pl.UTF-8):	Pakiet LaTeXa media9
Name:		tex-latex-media9
Version:	1.25
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing
Source0:	http://mirrors.ctan.org/macros/latex/contrib/media9.zip
# Source0-md5:	70b4be25f2e34d4875906d44fd769869
URL:		https://gitlab.com/agrahn/media9
BuildRequires:	/usr/bin/tex
BuildRequires:	rpmbuild(macros) >= 1.751
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
# TODO: use generic
Requires:	texlive
Provides:	tex(media9) = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an interface to embed interactive Flash (SWF)
and 3D objects (Adobe U3D & PRC) as well as video and sound files or
streams in the popular MP4, FLV, MP3 formats into PDF documents with
Acrobat-9/X compatibility. Playback of multimedia files relies on
Adobe Flash Player which supports the efficient H.264 codec for video
compression.

This package is based on the RichMedia Annotation, an Adobe addition
to the PDF specification. It replaces the now obsolete movie15
package.

Note that Adobe Reader for Linux has dropped Flash support since
version 9.4.2.

%description -l pl.UTF-8
Ten pakiet dostarcza interfejs do osadzania obiektów interaktywnego
Flasha (SWF) oraz 3D (Adobe U3D i PRC), a także plików/strumieni
filmów oraz dźwiękowych w popularnych formatach MP4, FLV, MP3 w
dokumentach PDF w sposób zgodny z Actobatem 9/X. Odtwarzanie plików
multimedialnych jest oparte na Adobe Flash Playerze, który obsługuje
kodek kompresji obrazu H.264.

Ten pakiet jest oparty na znacznikach RichMedia Annotation - dodatku
Adobe do specyfikacji PDF. Zastępuje przestarzały pakiet movie15.

Uwaga: Adobe Reader dla Linuksa od wersji 9.4.2 nie ma obsługi Flasha.

%prep
%setup -q -n media9

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{doc/latex,tex/latex}/media9

cp -p doc/*.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/media9
cp -p *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/media9

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%doc %{_datadir}/texmf/doc/latex/media9
%{_datadir}/texmf/tex/latex/media9
