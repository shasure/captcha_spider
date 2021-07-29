#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: kerlomz <kerlomz@gmail.com>
import hashlib
import multiprocessing as mul
import os
from typing import Union

from utils import Project, ServiceType, Charset


class CustomProject(Project):
    """
    定义自己的类
    """

    def __init__(self,
                 service_type: ServiceType = None,
                 captcha_url: str = None,
                 captcha_feedback_url: str = None,
                 captcha_length: Union[list, int] = None,
                 captcha_charset: Charset = Charset.UNDEFINED,
                 platform_type: str = None, ):
        super().__init__(
            service_type,
            captcha_url,
            captcha_feedback_url,
            captcha_length,
            captcha_charset,
            platform_type)

    def feedback_process(self, captcha_text: str) -> bool:
        """
        :param captcha_text: 验证码识别结果
        :return: 返回验证状态 [验证码正确, 验证码错误]
        """
        # 提交captcha，判断captcha对错
        data = {'login_name': 'admin',
                'pass_word': hashlib.md5(os.urandom(4)).hexdigest(),
                'codevalidate': captcha_text}
        formpost_res = self.session.post(self._captcha_feedback_url, data)
        if "验证码错误" in formpost_res.text:
            return False
        return True


def start_project(project, captcha_num):
    project.start(captcha_num)


if __name__ == '__main__':

    project_ddddocr = CustomProject(
        captcha_length=4,
        captcha_charset=Charset.ALPHANUMERIC,
        service_type=ServiceType.ddddocr,
        captcha_url="http://12349.mzj.nanjing.gov.cn/code/1627189499057",
        captcha_feedback_url="http://12349.mzj.nanjing.gov.cn/admin/beforeLogin"
    )

    project_sixsixocr = CustomProject(
        captcha_length=4,
        captcha_charset=Charset.ALPHANUMERIC,
        service_type=ServiceType.sixsixocr,
        captcha_url="http://12349.mzj.nanjing.gov.cn/code/1627189499057",
        captcha_feedback_url="http://12349.mzj.nanjing.gov.cn/admin/beforeLogin"
    )
    pool = mul.Pool(2)
    for project in [project_ddddocr, project_sixsixocr]:
        pool.apply_async(start_project, (project, 100))
    pool.close()
    pool.join()

    print("finished.")
