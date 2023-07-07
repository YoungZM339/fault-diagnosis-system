from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class DiagnosisTask(models.Model):
    owner = models.ForeignKey(User, verbose_name="归属的用户", on_delete=models.CASCADE)
    uploaded_file = models.FileField(upload_to='uploaded_files/', verbose_name="上传的文件")
    diagnosis_result_file = models.FileField(upload_to='diagnosis_result_file/', verbose_name="诊断结果文件")
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    DIAGNOSIS_STATUS_PENDING = 'pending'
    DIAGNOSIS_STATUS_PROCESSING = 'processing'
    DIAGNOSIS_STATUS_COMPLETED = 'completed'
    DIAGNOSIS_STATUS_CHOICES = (
        (DIAGNOSIS_STATUS_PENDING, '等待中'),
        (DIAGNOSIS_STATUS_PROCESSING, '处理中'),
        (DIAGNOSIS_STATUS_COMPLETED, '已完成'),
    )
    diagnosis_status = models.CharField(verbose_name="诊断任务状态", max_length=50, choices=DIAGNOSIS_STATUS_CHOICES,
                                        default=DIAGNOSIS_STATUS_PENDING)

    class Meta:
        verbose_name = "诊断任务"
        ordering = ("-created",)

    def __str__(self):
        return f"{self.owner.username}'s diagnosis task: {self.uploaded_file.name}"


class TrainTask(models.Model):
    owner = models.ForeignKey(User, verbose_name="归属的用户", on_delete=models.CASCADE)
    uploaded_file = models.FileField(upload_to='uploaded_files/', verbose_name="上传的文件")
    train_result_file = models.FileField(upload_to='train_result_file/', verbose_name="训练结果文件")
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    TRAIN_STATUS_PENDING = 'pending'
    TRAIN_STATUS_PROCESSING = 'processing'
    TRAIN_STATUS_COMPLETED = 'completed'
    TRAIN_STATUS_CHOICES = (
        (TRAIN_STATUS_PENDING, '等待中'),
        (TRAIN_STATUS_PROCESSING, '处理中'),
        (TRAIN_STATUS_COMPLETED, '已完成'),
    )
    train_status = models.CharField(verbose_name="诊断任务状态", max_length=50, choices=TRAIN_STATUS_CHOICES,
                                    default=TRAIN_STATUS_PENDING)

    class Meta:
        verbose_name = "训练任务"
        ordering = ("-created",)

    def __str__(self):
        return f"{self.owner.username}'s train task: {self.uploaded_file.name}"
