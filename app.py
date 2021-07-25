#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: kerlomz <kerlomz@gmail.com>
import multiprocessing as mul


def start_project(project, captcha_num):
    project.start(captcha_num)


if __name__ == '__main__':
    # Type - 1
    # from spiders.demo import Baidu
    # project = Baidu()
    # project.configuration(
    #     save_false=True,
    #     headers={
    #         "Cookie": "填入自己的Cookie"
    #     }
    # )
    # project.start(num=100000)

    # Type - 2
    from utils import Project, ServiceType, Charset

    project_ddddocr = Project(
        captcha_length=4,
        captcha_charset=Charset.ALPHANUMERIC,
        service_type=ServiceType.ddddocr,
        captcha_url="http://12349.mzj.nanjing.gov.cn/code/1627189499057",
        captcha_feedback_url="http://12349.mzj.nanjing.gov.cn/admin/beforeLogin"
    )

    project_sixsixocr = Project(
        captcha_length=4,
        captcha_charset=Charset.ALPHANUMERIC,
        service_type=ServiceType.sixsixocr,
        captcha_url="http://12349.mzj.nanjing.gov.cn/code/1627189499057",
        captcha_feedback_url="http://12349.mzj.nanjing.gov.cn/admin/beforeLogin"
    )
    pool = mul.Pool(2)
    for project in [project_ddddocr, project_sixsixocr]:
        pool.apply_async(start_project, (project, 11000))
    pool.close()
    pool.join()

    print("finished.")
