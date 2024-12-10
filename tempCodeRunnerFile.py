= 10  # 10点アップ
            bird.change_img(6, screen)  # こうかとん喜びエフェクト

        for bomb in pg.sprite.groupcollide(bombs, gravitys, True, True).keys():  # gravityと衝突した爆弾リスト
            exps.add(Explosion(bomb, 50))  # 爆発エフェクト #爆発した位置にエフェクトを表示
        
        for emy