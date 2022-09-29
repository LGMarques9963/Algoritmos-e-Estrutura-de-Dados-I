x_merchantid 	url_merchant 	    ativo 	
043 	aciumbrasil.myshopify.com	NULL
473 	www.visto.bio 	            NULL
513 	evibrasil.com.br 	        NULL
582 	www.biossance.com.br 	    NULL
731 	www.descricao.com.br 	    NULL
756 	www.luz.vc 	                NULL
777 	www.shop.wemystic.com.br 	NULL
793 	www.editorawish.com.br 	    1
794 	adsavancado.com 	        NULL
802 	pampili.myshopify.com 	NULL
807 	nobrand-foods.myshopify.com 	NULL
809 	vinhos-franceses.myshopify.com 	NULL
818 	adrianakavietz.com 	NULL
822 	www.simpleorganic.com.br 	NULL
852 	br.store.ui.com 	NULL
898 	www.vestem.com 	NULL
899 	www.meubrinco.com 	NULL
907 	www.mofficer.com 	1
910 	www.samsonite.myshopify.com 	NULL
932 	moblylivre.myshopify.com 	NULL
943 	altaluce.myshopify.com 	NULL
949 	www.checkout.haight.com.br 	NULL



`merchants`.`x_merchantid` IN ('756','852','043','513','822','473', '910','702','898','802','582','949','777','818','794','809','932','793','899','907','943','807','731','756')

SELECT `merchants`.`x_merchantid`,`merchants_discount`.`merchants_id`,`merchants`.`url_merchant`,`merchants_discount`.`ativo`, `merchants_discount`.`payment_method`

FROM `merchants` LEFT JOIN `merchants_discount` ON `merchants`.`id` = `merchants_discount`.`merchants_id` WHERE 

`merchants`.`x_merchantid` IN ('756','852','043','513','822','473', '910','702','898','802','582','949','777','818','794','809','932','793','899','907','943','807','731','756')