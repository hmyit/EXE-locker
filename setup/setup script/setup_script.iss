; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "EXELocker"
#define MyAppVersion "1.0"
#define MyAppPublisher "EXELocker"
#define MyAppExeName "LockerDialog.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{1A0648C8-07D4-40BA-80C7-B7FAD7289EB2}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={pf}\{#MyAppName}
DisableProgramGroupPage=yes
OutputBaseFilename=exelocker_setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\LockerDialog.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\Include\*"; DestDir: "{app}\Include"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\qt4_plugins\*"; DestDir: "{app}\qt4_plugins"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\_ctypes.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\_win32sysloader.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\Crypto.Cipher._AES.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\Crypto.Hash._SHA256.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\Crypto.Random.OSRNG.winrandom.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\Crypto.Util._counter.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\LockerDialog.exe.manifest"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\mfc90.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\mfc90u.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\mfcm90.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\mfcm90u.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\Microsoft.VC90.CRT.manifest"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\Microsoft.VC90.MFC.manifest"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\msvcm90.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\msvcp90.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\msvcr90.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\PySide.QtCore.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\PySide.QtGui.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\PySide.QtNetwork.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\pyside-python2.7.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\python27.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\pythoncom27.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\pywintypes27.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\Qt3Support4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\QtCore4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\QtGui4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\QtNetwork4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\QtOpenGL4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\QtSql4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\QtSvg4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\QtXml4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\shiboken-python2.7.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\win32api.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\win32com.shell.shell.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\win32event.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\win32process.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\win32trace.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\win32ui.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Dropbox\work\new work\EXE locker\EXE_locker\dist\LockerDialog\base\*"; DestDir: "{app}\base"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Registry]
Root: HKLM; Subkey: "Software\EXELocker\Settings"; ValueType: string; ValueName: "InstallPath"; ValueData: "{app}"; Flags: uninsdeletekey

