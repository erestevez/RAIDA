from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import FileExtensionValidator
from upload_validator import FileTypeValidator



# Create your models here.

class registro(models.Model):

    def validate_aida(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Error de tamanno del archivo")


    chois = [
        ('Dirección General', 'Dirección General'),
        ('Dirección Adjunta', 'Dirección Adjunta'),
        ('Grupo de Desarrollo Estratégico', 'Grupo de Desarrollo Estratégico'),
        ('Grupo de Gestion Integrada de Proyectos-Productos', 'Grupo de Gestion Integrada de Proyectos-Productos'),
        ('Grupo de Negocios', 'Grupo de Negocios'),
        ('Grupo de Seguridad y Proteccion', 'Grupo de Seguridad y Proteccion'),
        ('Departamento de Inteligencia Empresarial', 'Departamento de Inteligencia Empresarial'),
        ('Grupo de Infraestructura', 'Grupo de Infraestructura'),
        ('Grupo de Desarrollo de Software', 'Grupo de Desarrollo de Software'),
        ('Grupo de Gestion de Informacion', 'Grupo de Gestion de Informacion'),
        ('Direccion de Economia', 'Direccion de Economia'),
        ('Departamento de Contabilidad y Finanzas', 'Departamento de Contabilidad y Finanzas'),
        ('Departamento de Planificacion y Estadisticas', 'Departamento de Planificacion y Estadisticas'),
        ('Dirección de Recursos Humanos', 'Dirección de Recursos Humanos'),
        ('Departamento de Gestión de Personal', 'Departamento de Gestión de Personal'),
        ('Departamento de Gestión de Formación', 'Departamento de Gestión de Formación'),
        ('Grupo de Salud Ocupacional', 'Grupo de Salud Ocupacional'),
        ('Departamento de Seguridad Integral y Medio Ambiente', 'Departamento de Seguridad Integral y Medio Ambiente'),
        ('Dirección de Logística', 'Dirección de Logística'),
        ('Departamento de Compra en Plaza', 'Departamento de Compra en Plaza'),
        ('Departamento de Almacenes', 'Departamento de Almacenes'),
        ('Almacén Central', 'Almacén Central '),
        ('Vicepresidencia de Producción', 'Vicepresidencia de Producción'),
        ('Grupo de Aseguramiento', 'Grupo de Aseguramiento'),
        ('Grupo para la Producción de Moringa', 'Grupo para la Producción de Moringa'),
        ('Dirección de Planta III', 'Dirección de Planta III'),
        ('Subdirección de Producción de IFA', 'Subdirección de Producción de IFA'),
        ('Departamento de Producción de Cultivos', 'Departamento de Producción de Cultivos'),
        ('Departamento de Purificación', 'Departamento de Purificación'),
        ('Departamento de Apoyo', 'Departamento de Apoyo'),
        ('Grupo de Leptospira', 'Grupo de Leptospira'),
        ('Departamento de Procesam. Aséptico y Envase', 'Departamento de Procesam. Aséptico y Envase'),
        ('Grupo de Formulación', 'Grupo de Formulación'),
        ('Grupo de Llenado, Liofilización y Revisión', 'Grupo de Llenado, Liofilización y Revisión'),
        ('Grupo de Etiquetado y Envase', 'Grupo de Etiquetado y Envase'),
        ('Grupo de Apoyo, Prep. y Esteriliz. de Materiales', 'Grupo de Apoyo, Prep. y Esteriliz. de Materiales'),
        ('Departamento Técnico Productivo', ' Departamento Técnico Productivo'),
        ('Grupo de Organización de la Producción', 'Grupo de Organización de la Producción'),
        ('Grupo de Documentación', 'Grupo de Documentación'),
        ('Grupo de Control de Procesos', 'Grupo de Control de Procesos'),
        ('Departamento de Servicios Auxiliares', 'Departamento de Servicios Auxiliares'),
        ('Grupo de Tratamiento de Aguas', 'Grupo de Tratamiento de Aguas'),
        ('Grupo de Prod. y Distrib. Vapor, Agua y Aire', 'Grupo de Prod. y Distrib. Vapor, Agua y Aire'),
        ('Grupo Electrógeno', 'Grupo Electrógeno'),
        ('Grupo de Supervisión', 'Grupo de Supervisión'),
        ('Departamento Administrativo de Planta III', 'Departamento Administrativo de Planta III'),
        ('Grupo Onco-BCG', 'Grupo Onco-BCG'),
        ('Dirección de Planta II', 'Dirección de Planta II'),
        ('Subdirección de Producción', 'Subdirección de Producción'),
        ('Grupo de Producción de Cultivos', 'Grupo de Producción de Cultivos'),
        ('Departamento de Producción de Tétanos', 'Departamento de Producción de Tétanos'),
        ('Grupo de Producción de Tétano', 'Grupo de Producción de Tétano'),
        ('Departamento de Apoyo y Purificación', 'Departamento de Apoyo y Purificación'),
        ('Grupo de Apoyo', 'Grupo de Apoyo'),
        ('Grupo de Purificación', 'Grupo de Purificación'),
        ('Grupo de Almacén y Logística', 'Grupo de Almacén y Logística'),
        ('Grupo de Climatización y Supervisión', 'Grupo de Climatización y Supervisión'),
        ('Grupo de Aguas Farmacéuticas', 'Grupo de Aguas Farmacéuticas'),
        ('Vicepresidencia de Investigación y Desarrollo', 'Vicepresidencia de Investigación y Desarrollo'),
        ('Grupo de Gerencia de Investigación y Desarrollo', 'Grupo de Gerencia de Investigación y Desarrollo'),
        ('Grupo de Logística', 'Grupo de Logística'),
        ('Subdirección de Investigaciones Básicas', 'Subdirección de Investigaciones Básicas'),
        ('Departamento de Investigaciones Básicas', 'Departamento de Investigaciones Básicas'),
        ('Grupo de Desarrollo de Productos', 'Grupo de Desarrollo de Productos'),
        ('Departamento de Evaluación de Productos', 'Departamento de Evaluación de Productos'),
        ('Grupo de Desarrollo Analítico', 'Grupo de Desarrollo Analítico'),
        ('Grupo de Evaluación Preclínica y Clínica', 'Grupo de Evaluación Preclínica y Clínica'),
        ('Departamento de Preclínica', 'Departamento de Preclínica'),
        ('Departamento Administrativo de Investigaciones', 'Departamento Administrativo de Investigaciones'),
        ('Dirección de Desarrollo Farmacéutico', 'Dirección de Desarrollo Farmacéutico'),
        ('Grupo de Formulación y Control de Procesos', 'Grupo de Formulación y Control de Procesos'),
        ('Grupo de Productos Homeopáticos', 'Grupo de Productos Homeopáticos'),
        ('Grupo de Productos Naturales', 'Grupo de Productos Naturales'),
        ('Departamento de Ensayos Clínicos', 'Departamento de Ensayos Clínicos'),
        ('Vicepresidencia Comercial', 'Vicepresidencia Comercial'),
        ('Departamento de Negocios y Ventas', 'Departamento de Negocios y Ventas'),
        ('Almacén de Productos Terminados', 'Almacén de Productos Terminados'),
        ('Grupo de Colaboración y Patentes', 'Grupo de Colaboración y Patentes'),
        ('Departamento de Registro Médico Sanitario', 'Departamento de Registro Médico Sanitario'),
        ('Departamento de Importaciones', 'Departamento de Importaciones'),
        ('Vicepresidencia de Calidad', 'Vicepresidencia de Calidad'),
        ('Grupo de Liofilización y Conservación de Cepas', 'Grupo de Liofilización y Conservación de Cepas'),
        ('Dirección de Control de la Calidad', 'Dirección de Control de la Calidad'),
        ('Grupo de Materias Primas', 'Grupo de Materias Primas'),
        ('Grupo Físico-Químico', 'Grupo Físico-Químico'),
        ('Grupo de Monitoreo', 'Grupo de Monitoreo'),
        ('Grupo de Bacteriología', 'Grupo de Bacteriología'),
        ('Grupo de Pruebas Biológicas', 'Grupo de Pruebas Biológicas'),
        ('Grupo de Cumplimiento de Buenas Prácticas', 'Grupo de Cumplimiento de Buenas Prácticas'),
        ('Departamento de Mejora', 'Departamento de Mejora'),
        ('Departamento de Validación y Metrología', 'Departamento de Validación y Metrología'),
        ('Grupo de Certificación de Lotes', 'Grupo de Certificación de Lotes'),
        ('Departamento Administrativo de Calidad', 'Departamento Administrativo de Calidad'),
        ('Departamento de Validación', 'Departamento de Validación'),
        ('Vicepresidencia Técnica', 'Vicepresidencia Técnica'),
        ('Dirección de Servicios Técnicos Ingenieros', 'Dirección de Servicios Técnicos Ingenieros'),
        ('Departamento de Organización y Control', 'Departamento de Organización y Control'),
        ('94', 'Subdirección de Ingeniería Planta'),
        ('Subdirección de Ingeniería Planta', 'Grupo de Mecánica y Termoenergía'),
        ('Grupo de Electrónica y Electricidad', 'Grupo de Electrónica y Electricidad'),
        ('Subdirección de Area Central', 'Subdirección de Area Central'),
        ('Departamento de Mecánica', 'Departamento de Mecánica'),
        ('Departamento de Electricidad', 'Departamento de Electricidad'),
        ('Departamento de Electrónica', 'Departamento de Electrónica'),
        ('Departamento de Termoenergía', 'Departamento de Termoenergía'),
        ('Grupo de Ingeniería de Investigaciones', 'Grupo de Ingeniería de Investigaciones'),
        ('Departamento de Inversiones', 'Departamento de Inversiones'),
        ('Departamento de Mantenimiento Constructivo', 'Departamento de Mantenimiento Constructivo'),
        ('Departamento Administrativo Casa Central', 'Departamento Administrativo Casa Central'),
        ('Departamento de Transporte', 'Departamento de Transporte'),
        ('Grupo de Producción y Ventas', 'Grupo de Producción y Ventas'),
        ('Organopónico', 'Organopónico'),
    ]
    usuario=models.CharField(max_length=50,unique=True)
    dirip = models.GenericIPAddressField(max_length=50,verbose_name="Direccion Ip",unique=True, protocol='IPv4')
    area = models.CharField(max_length=200, choices=chois,default='Areas')
    aida=models.FileField(upload_to='registros/static/aidas', verbose_name="Reporte Aida", validators=[validate_aida,FileTypeValidator(allowed_types=['text/htm','text/html','application/octet-stream']),FileExtensionValidator(allowed_extensions=['html','htm'])])
    inven=models.CharField(max_length=50,unique=True)
    sello=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.usuario
    def as_list(self):
        return [
            self.usuario,
            self.dirip,
            self.area,
            self.inven,
            self.sello,
        ]