from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os

def text_progres(index,max):
	try:
		if max<1:
			max += 1
		porcent = index / max
		porcent *= 100
		porcent = round(porcent)
		make_text = ''
		index_make = 1
		make_text += '\n['
		while(index_make<21):
			if porcent >= index_make * 5: make_text+='✭'
			else: make_text+='✩'
			index_make+=1
		make_text += ']\n'
		return make_text
	except Exception as ex:
			return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = '🔰ඞ Descargando🖤🔸🔸🔸 \n\n'
    msg+= '📔ඞ Nombre: ' + str(filename)+'\n'
    msg+= '⚖️ඞ Tamaño Total: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= '📥ඞ Descargado: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= '📨ඞ Velocidad: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= '⌛ඞ Tiempo: ' + str(datetime.timedelta(seconds=int(time))) +'\n\n'

    msg = '🔰ඞ Descargando Archivo🖤🔸🔸🔸\n\n'
    msg += '🗂️ඞ Archivo: '+filename+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += '📊ඞ Porcentaje: '+str(porcent(currentBits,totalBits))+'%\n'
    msg += '⚖️ඞ Total: '+sizeof_fmt(totalBits)+'\n'
    msg += '📥ඞ Descargado: '+sizeof_fmt(currentBits)+'\n'
    msg += '📨ඞ Velocidad: '+sizeof_fmt(speed)+'/s\n'
    msg += '⌛ඞ Tiempo de Descarga: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    if tid!='':
        msg+= '/cancel_' + tid
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = '🔰ඞ Subiendo A La Nube💜🔸🔸🔸\n\n'
    msg+= '📔ඞ Nombre: ' + str(filename)+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '📤Subiendo: ' + str(filename)+'\n'
    msg+= '⚖️ඞ Tamaño Total: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= '📦ඞ Subido: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= '📨ඞ Velocidad: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= '⌛ඞ Tiempo: ' + str(datetime.timedelta(seconds=int(time))) +'\n'

    msg = '🔰ඞ Subiendo A La Nube💜🔸🔸🔸\n\n'
    msg += '📔ඞ Nombre: '+filename+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '📚ඞ Parte: ' + str(filename)+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += '📊ඞ Porcentaje: '+str(porcent(currentBits,totalBits))+'%\n'
    msg += '⚖️ඞ Total: '+sizeof_fmt(totalBits)+'\n'
    msg += '📥ඞ Descargado: '+sizeof_fmt(currentBits)+'\n'
    msg += '📨ඞ Velocidad: '+sizeof_fmt(speed)+'/s\n'
    msg += '⌛ඞ Tiempo de Descarga: '+str(datetime.timedelta(seconds=int(time)))+'s\n'

    return msg
def createCompresing(filename,filesize,splitsize):
    msg = '🗜ඞ Comprimiendo💙🔸🔸🔸\n\n'
    msg+= '📔ඞ Nombre: ' + str(filename)+'\n'
    msg+= '⚖️ඞ Tamaño Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '🗂️ඞ Tamaño Partes: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= '🗃️ඞ Cantidad Partes: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,split_size,current,count,findex):
    msg = '💜ඞ Proceso Finalizado\n\n'
    msg+= '📔ඞ Nombre: ' + str(filename)+'\n'
    msg+= '⚖️ඞ Tamaño Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '🗂️ඞ Tamaño Partes: ' + str(sizeof_fmt(split_size))+'\n'
    msg+= '📑ඞ Partes Subidas: ' + str(current) + '/' + str(count) +'\n\n'
    msg+= '🗑️ඞ Borrar Archivo: ' + '/del_'+str(findex)
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>🖇Enlaces🖇</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">🔗' + f['name'] + '🔗</a>'
            msg+= "<a href='"+url+"'>🔗"+f['name']+'🔗</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = '🗄️ඞ Archivos ('+str(len(evfiles))+')📑\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = '👤ඞ Condiguraciones De Usuario\n\n'
    msg+= '📔ඞ Nombre: @' + str(username)+'\n'
    msg+= '🗣️ඞ User: ' + str(userdata['moodle_user'])+'\n'
    msg+= '🔒ඞ Password: ' + str(userdata['moodle_password'])+'\n'
    msg+= '🔗ඞ Host: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= '🛠️ඞ RepoID: ' + str(userdata['moodle_repo_id'])+'\n'
    msg+= '🎫ඞ CloudType: ' + str(userdata['cloudtype'])+'\n'
    msg+= '🗄️ඞ UpType: ' + str(userdata['uploadtype'])+'\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= '📫ඞ Dir: /' + str(userdata['dir'])+'\n'
    msg+= '📚ඞ Tamaño de Zip : ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = 'No'
    if isadmin:
        msgAdmin = 'Si'
    msg+= '🔑ඞ Admin : ' + msgAdmin + '\n'
    proxy = 'NO'
    if userdata['proxy'] !='':
       proxy = 'SI'
    tokenize = 'NO'
    if userdata['tokenize']!=0:
       tokenize = 'SI'
    msg+= '📍ඞ Proxy : ' + proxy + '\n'
    msg+= '🔧ඞ Tokenize : ' + tokenize + '\n\n'
    msg+= '⚙️ඞ Configurar Moodle\n /acc user,password'
    return msg
